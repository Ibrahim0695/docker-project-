import logging
import sys
import importlib
import load

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