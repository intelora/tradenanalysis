from sqlalchemy import create_engine
import pandas as pd
import pymysql

def db_connect():
    try:
        db_connection_str = "mysql+pymysql://root:admin@localhost:3306/newschema"
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