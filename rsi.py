import pandas_ta as ta
import pandas as pd
import numpy as np
import executor

def rsi_buy_sell(df,risk):
    risk = float(risk[0])
    print("Starting RSI analysis")
    rsi_buy = []
    rsi_sell = []
    position = False
    rsi = ta.rsi(df['close'])
    df = pd.concat([df, rsi], axis=1).reindex(df.index)
    for i in range (len(df)):
        if df["RSI_14"][i] < 30:
            if position == False:
                rsi_buy.append(df['close'][i])
                rsi_sell.append(np.nan)
                position = True
            else:
                rsi_buy.append(np.nan)
                rsi_sell.append(np.nan)
        elif df["RSI_14"][i] > 70:
            if position == True:
                rsi_buy.append(np.nan)
                rsi_sell.append(df['close'][i])
                position = False
            else:
                rsi_buy.append(np.nan)
                rsi_sell.append(np.nan)
        else:
            rsi_buy.append(np.nan)
            rsi_sell.append(np.nan)
    print("RSI Analysis completed")
    df['buy_signal_price'], df['sell_signal_price'] = pd.Series([rsi_buy, rsi_sell])
    df["strategy_name"]="rsi_{}".format(risk)
    df['indicator'] = "rsi"
    executor.clean_data(df)

        

