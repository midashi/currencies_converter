# 1. Приветствие
# 2. Мануал - как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 6. Подсчет
# 7. Вывод результата


# 1.
print("Добро пожаловать в конвертатор валют!")

# 2.
print('''
Инструкция:
1. Ввести исходную валюту
2. Ввести результирующую валюту
3. Ввести количество валюты
''')

CURRENCIES = get_available_currencies()

if CURRENCIES:
    print("Доступные валюты:" + .join(CURRENCIES))
    from_currency = input_currency("Введите исходную валюту:")
    to_currency = input_currency("Введите результирующую валюту:")   
else:
    print("Извините. Список доступных валют пока недоступен. Попробуйте позже")

def input_currency(prompt, CURRENCIES):
    while True:
        user_input = input(prompt).strip().upper()
        if not user_input:
            print("Ошибка ввода. Ввеcти можно только валюту из списка доступных валют.")
            continue
        if user_input in CURRENCIES:
            return user_input
        else:
            print("Ошибка ввода. Ввеcти можно только валюту из списка доступных валют.")

amount = input("Введите количество:")

def convert(amount, from_currency, to_currency, CURRENCIES):

    from_value = CURRENCIES.get(from_currency)
    to_value = CURRENCIES.get(to_currency)   

    coefficient = to_value / from_value
    return round(amount * coefficient, 2)

result = convert(float(amount), from_currency, to_currency, CURRENCIES)

print(f'{amount} {from_currency} = {result} {to_currency}')
