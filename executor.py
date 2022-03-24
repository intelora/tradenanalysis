import db_connect
import pandas as pd

def clean_data(df):
    print("Starting Cleaning Data")
    # a = data.dropna(subset=["buy_signal_price"])
    # b = data.dropna(subset=["sell_signal_price"])
    # x = a.append(b)
    # new_data = x.drop(labels=["open","close","high","low","index"],axis=1)
    df1 = df.dropna(subset=['sell_signal_price'], axis = 0)  #'buy_signal_price'
    df = pd.concat([df,df1])
    new_data = df.drop(labels=["open","close","high","low","index"],axis=1)
    print("Data Cleaning Completed")
    return db_connect.update_to_db(new_data)



