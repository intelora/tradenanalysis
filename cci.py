import pandas as pd 
import pandas_ta as ta
import numpy as np
import executor

def cci_buy_sell(df,risk):
    risk = float(risk[0])
    print("starting CCI analysis")
    cci_buy = []
    cci_sell = []
    position = False
    cci = ta.cci(df['high'],df['low'],df['close'])
    df = pd.concat([df, cci], axis=1).reindex(df.index)
    df.rename(columns = {"CCI_14_0.015":"CCI_line"},inplace=True)
    print(df)
    upper_band = 150
    Lower_band = (-150)
    for i in range(len(df)):
        if df['CCI_line'][i] < Lower_band :
            if position == False:
                cci_buy.append(df['close'][i])
                cci_sell.append(np.nan)
                position = True
            else:
                cci_buy.append(np.nan)
                cci_sell.append(np.nan)
        elif df['CCI_line'][i] > upper_band:
            if position == True:
                cci_buy.append(np.nan)
                cci_sell.append(df['close'][i])
                position = True
            else:
                cci_buy.append(np.nan)
                cci_sell.append(np.nan)
        else:
            cci_buy.append(np.nan)
            cci_sell.append(np.nan)
    print("CCi Analysis completed")
    df['buy_signal_price'], df['sell_signal_price'] = pd.Series([cci_buy, cci_sell])
    df["strategy_name"]="cci_{}".format(risk)
    df['indicator'] = "cci"
    executor.clean_data(df)