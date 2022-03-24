import pandas as pd
import numpy as np
import pandas_ta as ta
import executor

def tsi_buy_sell(df,risk):
    risk = float(risk[0])
    print("starting CCI analysis")
    tsi_buy = []
    tsi_sell = []
    position = False
    tsi = ta.tsi(df['close'])
    df = pd.concat([df, tsi], axis=1).reindex(df.index)
    df.rename(columns = {"TSI_13_25_13":"TSI_line","TSIs_13_25_13":"Signal_line"},inplace=True)
    # print(df)
    for i in range(len(df)):
        if df['TSI_line'][i] > df['Signal_line'][i]:
            if position == False:
                tsi_buy.append(df['close'][i])
                tsi_sell.append(np.nan)
                position = True
            else:
                tsi_buy.append(np.nan)
                tsi_sell.append(np.nan)
        elif df['TSI_line'][i] < df['Signal_line'][i]:
            if position == True:
                tsi_buy.append(np.nan)
                tsi_sell.append(df['close'][i])
                position = False
            else:
                tsi_buy.append(np.nan)
                tsi_sell.append(np.nan)
        else:
            tsi_buy.append(np.nan)
            tsi_sell.append(np.nan)
    print("TSI Analysis completed")
    df['buy_signal_price'], df['sell_signal_price'] = pd.Series([tsi_buy, tsi_sell])
    df["strategy_name"]="tsi_{}".format(risk)
    df['indicator'] = "tsi"
    executor.clean_data(df)