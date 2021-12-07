import pandas_ta as ta
import numpy as np
import pandas as pd
import db_connect
#SMA BUY SELL
#Function for buy and sell signal


indicator = {
    "SMA": "sma",
    "EMA":"ema",
    "WMA":"wma",
    "MACD":"macd",
    "RSI":"rsi",
    "CCI":"cci",
    "STOCH":"stoch",
    "BBANDS":"bbands",
    
}




def sma_buy_sell(data,values):
    signal1,signal2 = values
    sma_value_1 = "sma_{}".format(signal1)
    sma_value_2 = "sma_{}".format(signal2)
    data["col1"] = ta.sma(data['close'],signal1)
    data["col2"] = ta.sma(data['close'],signal2)
    signalBuy = []
    signalSell = []
    position = False 

    for i in range(len(data)):
        if data[sma_value_1][i] > data[sma_value_2][i]:
            if position == False :
                signalBuy.append(data['close'][i])
                signalSell.append(np.nan)
                position = True
            else:
                signalBuy.append(np.nan)
                signalSell.append(np.nan)
        elif data[sma_value_1][i] < data[sma_value_2][i]:
            if position == True:
                signalBuy.append(np.nan)
                signalSell.append(data['close'][i])
                position = False
            else:
                signalBuy.append(np.nan)
                signalSell.append(np.nan)
        else:
            signalBuy.append(np.nan)
            signalSell.append(np.nan)
    
    data['buy_signal_price'], data['sell_signal_price'] = pd.Series([signalBuy, signalSell])
    data["strategy_name"]="sma_{}_{}".format(sma_value_1,sma_value_2)
    data['indicator'] = "sma"
    clean_data(data=data,values=values)

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