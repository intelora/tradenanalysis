import sma,macd,ema

def calculate_for_indicator(script_df,indicator,args):
    if str(indicator).upper() == "SMA":
            sma.sma_buy_sell(script_df,args)
    elif str(indicator).upper() == "MACD":
        macd.MACD_Strategy(script_df,args)
    if str(indicator).upper() == "EMA":
            ema.ema_buy_sell(script_df,args)