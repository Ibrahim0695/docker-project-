import os

from sqlalchemy import URL, create_engine
from dotenv import load_dotenv


load_dotenv()

def load_coins(coinz_df):

    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')

    url = URL.create(
        'postgresql+psycopg2',
        username=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=int(DATABASE_PORT),
        database=DATABASE_NAME,
    )
    engine = create_engine(url)
    try:
        with engine.begin() as connection:
            coinz_df.to_sql('coins', connection, if_exists='replace', index=False)
    finally:
        engine.dispose()

   