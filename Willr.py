import pandas as pd
import numpy as np
import pandas_ta as ta
import executor

def willr_buy_sell(df,risk):
    risk = float(risk[0])
    print("starting willR analysis")
    willr_buy = []
    willr_sell = []
    position = False
    willr = ta.willr(df['high'],df['low'],df['close'])
    df = pd.concat([df,willr], axis=1).reindex(df.index)
    print("\n",df)
    for i in range(len(df)):
        if df['WILLR_14'][i] < -80 :
            if position == False:
                willr_buy.append(df['close'][i])
                willr_sell.append(np.nan)
                position = True
            else:
                willr_buy.append(np.nan)
                willr_sell.append(np.nan)
        elif df['WILLR_14'][i] > -20 :
            if position == True:
                willr_buy.append(np.nan)
                willr_sell.append(df['close'][i])
                position = True
            else:
                willr_buy.append(np.nan)
                willr_sell.append(np.nan)
        else:
            willr_buy.append(np.nan)
            willr_sell.append(np.nan)
    
    df['buy_signal_price'],df['sell_signal_price'] = pd.Series([willr_buy,willr_sell]) 
    df["strategy_name"]="willr_{}".format(risk)
    df['indicator'] = "willr"
    #  print(">>>>>>>>>>>>>>>>>>>>>>\n", df[0])
    df = df.drop(df.columns[[1]],axis=1)
    df.rename(columns = {"Date":"Trade_Date","time":"Trade_time"},inplace=True)
    print("WILLR Analysis completed\n", df)
    for i in df.columns:
     print(i)
    executor.clean_data(df)     