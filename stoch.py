import pandas as pd
import pandas_ta as ta
import numpy as np
import executor

def stoch_buy_sell(df,risk):
    risk = float(risk[0])
    stoch_buy = []
    stoch_sell = []
    position = False
    stoch = ta.stoch(df['high'], df['low'], df['close'])
    df = pd.concat([df, stoch], axis=1).reindex(df.index)
    print(df)
    for i in range (len(df)):
        if df['STOCHk_14_3_3'][i] < 20 and df['STOCHd_14_3_3'][i] < 20 and df['STOCHk_14_3_3'][i] < df['STOCHd_14_3_3'][i] :
            if position == False:
                stoch_buy.append(df['close'][i])
                stoch_sell.append(np.nan)
                position =True
            else:
                stoch_buy.append(np.nan)
                stoch_sell.append(np.nan)
        elif df['STOCHk_14_3_3'][i] > 80 and df['STOCHd_14_3_3'][i] > 80 and df['STOCHk_14_3_3'][i] > df['STOCHd_14_3_3'][i] :
            if position == True:
                stoch_buy.append(np.nan)
                stoch_sell.append(df['close'][i])
                position = False
            else:
                stoch_buy.append(np.nan)
                stoch_sell.append(np.nan)
        else:
            stoch_buy.append(np.nan)
            stoch_sell.append(np.nan)
    print("stoch Analysis completed")
    df['buy_signal_price'],df['sell_signal_price'] = pd.Series([stoch_buy,stoch_sell]) 
    df["strategy_name"]="stoch_{}".format(risk)
    df['indicator'] = "stoch"
    executor.clean_data(df)