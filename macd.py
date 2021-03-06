import pandas_ta as ta
import numpy as np
import executor
import pandas as pd

def MACD_Strategy(df, risk):
    risk = float(risk[0])
    print("starting macd analysis")
    MACD_Buy=[]
    MACD_Sell=[]
    position=False
    macd = ta.macd(df['close'])
    macd.rename(columns = {"MACD_12_26_9":"col1","MACDh_12_26_9":"col2","MACDs_12_26_9":"col3"},inplace=True)

    df = pd.concat([df, macd], axis=1).reindex(df.index)
    for i in range(0, len(df)):
        if df['col1'][i] > df["col3"][i] :
            MACD_Sell.append(np.nan)
            if position ==False:
                MACD_Buy.append(df['close'][i])
                position=True
            else:
                MACD_Buy.append(np.nan)
        elif df['col1'][i] < df["col3"][i] :
            MACD_Buy.append(np.nan)
            if position == True:
                MACD_Sell.append(df['close'][i])
                position=False
            else:
                MACD_Sell.append(np.nan)
        elif position == True and df['close'][i] < MACD_Buy[-1] * (1 - risk):
            MACD_Sell.append(df["close"][i])
            MACD_Buy.append(np.nan)
            position = False
        elif position == True and df['close'][i] < df['close'][i - 1] * (1 - risk):
            MACD_Sell.append(df["close"][i])
            MACD_Buy.append(np.nan)
            position = False
        else:
            MACD_Buy.append(np.nan)
            MACD_Sell.append(np.nan)
    print("MACD Analysis completed")
    df['buy_signal_price'], df['sell_signal_price'] = pd.Series([MACD_Buy, MACD_Sell])
    df["strategy_name"]="macd_{}".format(risk)
    df['indicator'] = "macd"
    executor.clean_data(df)
    
