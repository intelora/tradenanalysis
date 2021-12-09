import db_connect

def clean_data(data):
    print("Starting Cleaning Data")
    a = data.dropna(subset=["buy_signal_price"])
    b = data.dropna(subset=["sell_signal_price"])
    x = a.append(b)
    new_data = x.drop(labels=["open","close","high","low","index"],axis=1)
    print("Data Cleaning Completed")
    return db_connect.update_to_db(new_data)
