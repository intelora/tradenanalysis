import pandas as pd
import sys,db_connect
import sma
import macd


path0 = sys.argv
path = r"{}".format(path0[1])

# demo path
# path = r"C:\Users\user\Desktop\aswath\tradenanalysis\script.csv"

script = ""
indicator = ""
args = []
# bnf_pd = db_connect.get_data_as_dataframe("BANKNIFTY")

# bnf_pd = pd.read_csv("banknifty.csv")


path_data = pd.read_csv(filepath_or_buffer = path)
path_list = path_data.values.tolist()
for values in path_list:
    script, indicator, *args = values
    a = db_connect.get_data_as_dataframe(script)
    print("No of rows and columns", a.shape)
    #connect to databse
    print("Processing current strategy ", indicator)
    print(script,indicator,args)
    if str(indicator).upper() == "SMA":
        sma.sma_buy_sell(a,args)
    elif str(indicator).upper() == "MACD":
        macd.MACD_Strategy(a,args)

