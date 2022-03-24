import pandas as pd
import numpy as np
import pandas_ta as ta
import executor 

def adx_buy_sell(df,risk):
    risk = float(risk[0])
    print("starting ADX analysis")
    adx_buy = []
    adx_sell = []
    position = False
    adx = ta.adx(df['high'],df['low'],df['close'])
    df = pd.concat([df, adx], axis=1).reindex(df.index)
    # print(df)
    for i in range(len(df)):
        # print("aaaaaaaaaaaaaaaaaaaa")
        # print("== ",(["ADX_14")[i])
        # print("bbbbbbbbbbbbbbbbbbb")
        if df["ADX_14"][i] > 25 and df["DMP_14"][i] > df["DMN_14"][i]:
            if position == False:
                adx_buy.append(df['close'][i])
                adx_sell.append(np.nan)
                position = True
            else:
                adx_buy.append(np.nan)
                adx_sell.append(np.nan)
        elif df["ADX_14"][i] > 25 and df["DMN_14"][i] > df["DMP_14"][i]:
            if position == True:
                adx_buy.append(np.nan)
                adx_sell.append(df['close'][i])
                position = False
            else:
                adx_buy.append(np.nan)
                adx_sell.append(np.nan)
        else:
            adx_buy.append(np.nan)
            adx_sell.append(np.nan)
    print("ADX Analysis completed")
    df['buy_signal_price'], df['sell_signal_price'] = pd.Series([adx_buy, adx_sell])
    df["strategy_name"]="adx_{}".format(risk)
    df['indicator'] = "adx"
    executor.clean_data(df)