import json
import requests

def extract_coins():
    

    url = "https://api.coinpaprika.com/v1/tickers?quotes=USD"

    response = requests.get(url)

    response_json = response.json()

    coin_list= response_json[:5]

    return coin_list


    