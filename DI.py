import pandas as pd
import numpy as np
import pandas_ta as ta
import executor

def di_buy_sell(df,risk):
    risk = float(risk[0])
    di_buy = []
    di_sell = []
    position = False
    di = ta.