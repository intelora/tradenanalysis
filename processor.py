import db_connect
import indicator_manager

def process(path_list):
    existing_script = {}
    script = ""
    script_df =None
    indicator = ""
    args = []
    for values in path_list:
        script, indicator, *args = values
        try:
            script_df = existing_script[script]
            print("Script already exists in memory")
        except KeyError:
            print(f"getting script {script}  from database")
            script_df = db_connect.get_data_as_dataframe(script)
            existing_script[script] = script_df
            print("No of rows and columns", script_df.shape)
        print("Processing current strategy ", indicator)
        print(script,indicator,args)
        indicator_manager.calculate_for_indicator(script_df,indicator,args)        

