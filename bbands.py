import pandas_ta as ta
import numpy as np
import pandas as pd
import executor

def bbands_buy_sell(data,risk):
    print("Starting bbands Analysis")
    risk = float(risk[0])
    bbands = ta.bbands(data['close']) 
    # bbands.rename(columns = {"BBL_20_2":"col1","BBU_20_2":"col2"},inplace=True)
    bbandsBuy = []
    bbandsSell = []
    position = False 
    data = pd.concat([data,bbands],axis=1).reindex(data.index)
    print(data)
    for i in data.columns:
        print(i)
    for i in range(len(data)):
        if data['close'][i] < data["BBL_5_2.0"][i]: 
            if position == False :
                bbandsBuy.append(data['close'][i])
                bbandsSell.append(np.nan)
                position = True
            else:
                bbandsBuy.append(np.nan)
                bbandsSell.append(np.nan)
        elif data['close'][i] > data["BBU_5_2.0"][i]:
            if position == True:
                bbandsBuy.append(np.nan)
                bbandsSell.append(data['close'][i])
                position = False
            else:
                bbandsBuy.append(np.nan)
                bbandsSell.append(np.nan)
        else:
            bbandsBuy.append(np.nan)
            bbandsSell.append(np.nan)
    print("Sucessfully Completed bbands Analysis")
    data['buy_signal_price'], data['sell_signal_price'] = pd.Series([bbandsBuy, bbandsSell])
    data["strategy_name"]="bbands_{}".format(risk)
    data['indicator'] = "bbands"
    executor.clean_data(data)