import pandas as pd
import numpy as np
import pandas_ta as ta
import executor

def kc_buy_sell(df,risk):
    risk = float(risk[0])
    print("starting KC analysis")
    kc_buy = []
    kc_sell = []
    position = False
    kc = ta.kc(df['high'],df['low'],df['close'])
    df = pd.concat([df, kc], axis=1).reindex(df.index)
    print(df)
    for i in range(len(df)):
        if df['close'][i] < df['KCLe_20_2'][i]:
            if position == False:
                kc_buy.append(df['close'][i])
                kc_sell.append(np.nan)
                position = True
            else:
                kc_buy.append(np.nan)
                kc_sell.append(np.nan)
        elif df['close'][i] > df['KCUe_20_2'][i]:
            if position == True:
                kc_buy.append(np.nan)
                kc_sell.append(df['close'][i])
                position = False
            else:
                kc_buy.append(np.nan)
                kc_sell.append(np.nan)
        else:
            kc_buy.append(np.nan)
            kc_sell.append(np.nan)
    print("KC Analysis completed")
    df['buy_signal_price'], df['sell_signal_price'] = pd.Series([kc_buy, kc_sell])
    df["strategy_name"]="kc_{}".format(risk)
    df['indicator'] = "kc"
    executor.clean_data(df)
    