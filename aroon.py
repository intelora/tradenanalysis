import pandas as pd
import numpy as np
import pandas_ta as ta
import executor

def aroon_buy_sell(df,risk):
    risk = float(risk[0])
    aroon_buy = []
    aroon_sell = []
    position = False
    aroon = ta.aroon(df['high'],df['low'])
    df = pd.concat([df,aroon], axis=1).reindex(df.index)
    print(df)
    for i in range(len(df)):
        if df['AROONU_14'][i] >= 70 and df['AROOND_14'][i] <= 30:
            if position == False:
                aroon_buy.append(df['close'][i])
                aroon_sell.append(np.nan)
                position = True
            else:
                aroon_buy.append(np.nan)
                aroon_sell.append(np.nan)
        elif df['AROONU_14'][i] <= 30 and df['AROOND_14'][i] >= 70:
            if position == True:
                aroon_buy.append(np.nan)
                aroon_sell.append(df['close'][i])
            else:
                aroon_buy.append(np.nan)
                aroon_sell.append(np.nan)
        else:
            aroon_buy.append(np.nan)
            aroon_sell.append(np.nan)
    print("AROON Analysis completed")
    df['buy_signal_price'],df['sell_signal_price'] = pd.Series([aroon_buy,aroon_sell]) 
    df["strategy_name"]="aroon_{}".format(risk)
    df['indicator'] = "aroon"
    executor.clean_data(df)
