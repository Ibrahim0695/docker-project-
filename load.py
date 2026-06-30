import os

from sqlalchemy import create_engine, text
from dotenv import load_dotenv


load_dotenv()

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

   