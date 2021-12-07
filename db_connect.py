from sqlalchemy import create_engine
import pandas as pd


def db_connect():
    try:
        db_connection_str = 'mysql+pymysql://intelaku_nse_aswath:intelaku_nse_aswath@intelora.co.in:3306/intelaku_nse_aswath'
        db_connection = create_engine(db_connection_str)
    
        return db_connection
    except Exception as e:
        print(e,e.args)
        return None


def get_data_as_dataframe(ticker):
    try:
        db_call = "select * from {}".format(ticker)
        frame = pd.read_sql(db_call, db_connect());
        return frame
    except Exception as e:
        print(e,e.args)
        return 



