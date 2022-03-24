import pandas as pd
import numpy as np
import pandas_ta as ta
import executor

def coppock_buy_sell(df,risk):
    risk = float(risk[0])
    coppock_buy = []
    coppock_sell = []
    position = False
    coppock = ta.coppock(df['close'])
    df = pd.concat([df, coppock], axis=1).reindex(df.index)
    print(df)
    for i in range(len(df)):
        if df['COPC_11_14_10'][i] > 0:
            if position == False:
                coppock_buy.append(df['close'][i])
                coppock_sell.append(np.nan)
                position == True
            else:
                coppock_buy.append(np.nan)
                coppock_sell.append(np.nan)
        elif df['COPC_11_14_10'][i] < 0:
            if position == True:
                coppock_buy.append(np.nan)
                coppock_sell.append(df['close'][i])
                position = False
            else:
                coppock_buy.append(np.nan)
                coppock_sell.append(np.nan)
        else:
            coppock_buy.append(np.nan)
            coppock_sell.append(np.nan)
    print("COPPOCK Analysis completed")
    df['buy_signal_price'],df['sell_signal_price'] = pd.Series([coppock_buy,coppock_sell]) 
    df["strategy_name"]="coppock_{}".format(risk)
    df['indicator'] = "coppock"
    executor.clean_data(df)

