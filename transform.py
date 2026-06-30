import pandas as pd

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

