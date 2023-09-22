import requests

API_KEY = "fca_live_njqwvI7anX8wysCfy3BSFk2jEeWKd3SgXoZUrNP8"
API_URL = "https://api.freecurrencyapi.com/v1/latest?apikey="

def get_actual_currencies():
    response = requests.get(URL + API_KEY)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
