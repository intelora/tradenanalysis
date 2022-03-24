
#----------------------------------------------Not Completed-----------------------------------------------------------
import pandas_ta as ta
import numpy as np
import pandas as pd
import executor

def bbands_buy_sell(data,values):
    print("Starting bbands Analysis")
    length1,std1 = values
    bbands = ta.bbands(data['close'],'''length=20,std=2''') 
    # bbands.rename(columns = {"BBL_20_2":"col1","BBU_20_2":"col2"},inplace=True)
    bbandsBuy = []
    bbandsSell = []
    position = False 
    data = pd.concat([data,bbands],axis=1).reindex(data.index)
    for i in range(len(data)):
        if data['close'][i] < data["BBL_20_2.0"][i]: 
            if position == False :
                bbandsBuy.append(data['close'][i])
                bbandsSell.append(np.nan)
                position = True
            else:
                bbandsBuy.append(np.nan)
                bbandsSell.append(np.nan)
        elif data['close'][i] > data["BBU_20_2.0"][i]:
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
    data["strategy_name"]="bbands_{}_{}".format(values)
    data['indicator'] = "bbands"
    executor.clean_data(data=data)