import db_connect
import macd

a = db_connect.get_data_as_dataframe("BANKNIFTY")


macd.MACD_Strategy(a,0.25)