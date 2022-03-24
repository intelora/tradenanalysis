import sys
import pandas as pd
import processor

# sample path
path = r"E:\TradeAnalytics\tradenanalysis\script.csv"

def readCSV(path):
    
    path_data = pd.read_csv(filepath_or_buffer = path)
    print("Finished Reading CSV file")
    path_list = path_data.values.tolist()
    print("Starting Process")
    processor.process(path_list)


if __name__=="__main__":
    # complete_path = sys.argv
    # print("Starting Program")
    # path = r"{}".format(complete_path[1])
    print("Reading CSV")
    readCSV(path) 