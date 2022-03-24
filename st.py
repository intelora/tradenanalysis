import pandas as pd
import numpy as np
import pandas_ta as ta
import executor
def st_buy_sell(df,risk):
    risk = float(risk[0])
    st_buy = []
    st_sell = []
    position = False
    st = ta.supertrend(df['high'],df['low'],df['close'])
    df = pd.concat([df,st], axis=1).reindex(df.index)
    print(df)
    for i in range(len(df)):
        if df['SUPERT_7_3.0'][i] < df['close'][i] :
            if position == False:
                st_buy.append(df['close'][i])
                st_sell.append(np.nan)
                position = True
            else:
                st_buy.append(np.nan)
                st_sell.append(np.nan)
        elif df['SUPERT_7_3.0'][i] > df['close'][i]:
            if position == True:
                st_buy.append(np.nan)
                st_sell.append(df['close'][i])
                position = False
            else:
                st_buy.append(np.nan)
                st_sell.append(np.nan)
        else:
            st_buy.append(np.nan)
            st_sell.append(np.nan)
    print("ST Analysis completed")
    df['buy_signal_price'],df['sell_signal_price'] = pd.Series([st_buy,st_sell]) 
    df["strategy_name"]="st_{}".format(risk)
    df['indicator'] = "st"
    executor.clean_data(df)


