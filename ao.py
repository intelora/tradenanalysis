import pandas as pd
import numpy as np
import pandas_ta as ta
import executor

def ao_buy_sell(df,risk):
    risk = float(risk[0])
    ao_buy = []
    ao_sell = []
    position = False
    ao = ta.ao(df['high'],df['low'])
    df = pd.concat([df,ao], axis=1).reindex(df.index)
    print(df)
    for i in range(len(df)):
        if df['AO_5_34'][i]> 0:
            if position == False:
                ao_buy.append(df['close'][i])
                ao_sell.append(np.nan)
                position = True
            else:
                ao_buy.append(np.nan)
                ao_sell.append(np.nan)
        elif df['AO_5_34'][i]< 0:
            if position == True:
                ao_buy.append(np.nan)
                ao_sell.append(df['close'][i])
                position = False
            else:
                ao_buy.append(np.nan)
                ao_sell.append(np.nan)
        else:
            ao_buy.append(np.nan)
            ao_sell.append(np.nan)
    print("AO Analysis completed")
    df['buy_signal_price'],df['sell_signal_price'] = pd.Series([ao_buy,ao_sell]) 
    df["strategy_name"]="ao_{}".format(risk)
    df['indicator'] = "ao"
    executor.clean_data(df)
