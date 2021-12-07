import pandas_ta as ta
import numpy as np
import db_connect
import pandas as pd

def MACD_Strategy(df, risk):
    MACD_Buy=[]
    MACD_Sell=[]
    macd = ta.macd(df['Close'])
    df = pd.concat([df, macd], axis=1).reindex(df.index)
    for i in range(0, len(df)):
        if df['MACD_12_26_9'][i] > df['MACDs_12_26_9'][i] :
            MACD_Sell.append(np.nan)
            if position ==False:
                MACD_Buy.append(df['Close'][i])
                position=True
            else:
                MACD_Buy.append(np.nan)
        elif df['MACD_12_26_9'][i] < df['MACDs_12_26_9'][i] :
            MACD_Buy.append(np.nan)
            if position == True:
                MACD_Sell.append(df['Close'][i])
                position=False
            else:
                MACD_Sell.append(np.nan)
        elif position == True and df['Close'][i] < MACD_Buy[-1] * (1 - risk):
            MACD_Sell.append(df["Close"][i])
            MACD_Buy.append(np.nan)
            position = False
        elif position == True and df['Close'][i] < df['Close'][i - 1] * (1 - risk):
            MACD_Sell.append(df["Close"][i])
            MACD_Buy.append(np.nan)
            position = False
        else:
            MACD_Buy.append(np.nan)
            MACD_Sell.append(np.nan)

    df['buy_signal_price'], df['sell_signal_price'] = pd.Series([MACD_Buy, MACD_Sell])
    df["strategy_name"]="macd_{}_{}".format(macd_value_1,macd_value_2)
    df['indicator'] = "sma"
    clean_data(df,values=values)

def clean_data(data,values):
    a = data.dropna(subset=["buy_signal_price"])
    b = data.dropna(subset=["sell_signal_price"])
    x = a.append(b)
    new_data = x.drop(labels=["open","close","high","low","index"],axis=1)
    return new_data
    

def update_to_db(data):
    try:
        con = db_connect.db_connect()
        data.to_sql("buy_sell_data",con,if_exists="append",index=False)
    except Exception as e:
        print(e)