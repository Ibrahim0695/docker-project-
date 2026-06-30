import json
import requests
import pandas as pd
import os
import logging
import sys
import importlib
import load

from sqlalchemy import create_engine, text
from dotenv import load_dotenv


load_dotenv()



def extract_coins():
    

    url = "https://api.coinpaprika.com/v1/tickers?quotes=USD"

    response = requests.get(url)

    response_json = response.json()

    coin_list= response_json[:5]

    return coin_list

def transform_coins(coin_list):
    coinz_df = pd.DataFrame(coin_list)
    coinz_df = coinz_df[[ 'name', 'symbol',  'total_supply', 'first_data_at', 'quotes' ]]
    coinz_df = coinz_df.rename(columns={ 'name': 'coin_name', 'first_data_at': 'invention_date'})                
    coinz_df["usd_price"] = coinz_df["quotes"].apply(lambda q: q["USD"]["price"])
    coinz_df = coinz_df.drop(columns=['quotes'])
    coinz_df["invention_date"] = pd.to_datetime(coinz_df["invention_date"], errors="coerce")
    coinz_df["invention_date"] = pd.to_datetime(coinz_df["invention_date"], errors="coerce")
    coinz_df["usd_price"] = coinz_df["usd_price"].round(4)
    coinz_df["total_supply"] = coinz_df["total_supply"].map("{:,.0f}".format)
    return coinz_df



def load_coins(coinz_df):
    
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')    

    try:
        engine = create_engine(
            f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
        )

        # Load DataFrame to PostgreSQL
        coinz_df.to_sql('coins', engine, if_exists='replace', index=False)
        

    except Exception as e:
        print(f"✗ Error loading data: {e}")

i

load = importlib.reload(load)

from extract import extract_coins
from transform import transform_coins
from load import load_coins


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def main():
    try:
        coin_list = extract_coins()
        coinz_df = transform_coins(coin_list)
        load_coins(coinz_df)
        print('ETL process completed successfully.')
    except Exception:
        logging.exception('ETL process failed')
        sys.exit(1)


if __name__ == "__main__":
    main()  
    