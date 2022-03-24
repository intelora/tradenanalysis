import pandas as pd
import numpy as np
import pandas_ta as ta
import executor

def kst_buy_sell(df,risk):
    risk = float(risk[0])
    print("starting ADX analysis")
    kst_buy = []
    kst_sell = []
    position = False
    kst = ta.kst(df['close'])
    df = pd.concat([df, kst], axis=1).reindex(df.index)
    df.rename(columns = {"KST_10_15_20_30_10_10_10_15":"KST_line","KSTs_9":"signal_line"},inplace=True)
    print(df)
    for i in range(len(df)):
        if df['KST_line'][i] > df['signal_line'][i]:
            if position == False:
                kst_buy.append(df['close'][i])
                kst_sell.append(np.nan)
                position = True
            else:
                kst_buy.append(np.nan)
                kst_sell.append(np.nan)
        elif df['KST_line'][i] < df['signal_line'][i]:
            if position == True:
                kst_buy.append(np.nan)
                kst_sell.append(df['close'][i])
                position = True
            else:
                kst_buy.append(np.nan)
                kst_sell.append(np.nan)
        else:
            kst_buy.append(np.nan)
            kst_sell.append(np.nan)
    print("KST Analysis completed")
    df['buy_signal_price'],df['sell_signal_price'] = pd.Series([kst_buy,kst_sell]) 
    df["strategy_name"]="kst_{}".format(risk)
    df['indicator'] = "kst"
    executor.clean_data(df)
