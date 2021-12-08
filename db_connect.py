from sqlalchemy import create_engine
import pandas as pd
import pymysql

def db_connect():
    
    try:
        print("Connecting to database")
        db_connection_str = "mysql+pymysql://root:admin@localhost:3306/newschema"
        db_connection = create_engine(db_connection_str)
        print("databse connected")
        return db_connection
    except Exception as e:
        print(e,e.args)
        return None
    
def get_data_as_dataframe(ticker):
    try:
        print("convert databse into dataframe")
        db_call = "select * from {}".format(ticker)
        frame = pd.read_sql(db_call, db_connect());
        print("Conversion Completed")
        return frame
    except Exception as e:
        print(e,e.args)
        return 