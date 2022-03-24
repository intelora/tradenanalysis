import sma,macd,ema,bbands
import rsi
import adx,kst,cci,tsi,kc,Willr
import RVI,aroon,ao,st,stoch,coppock
def calculate_for_indicator(script_df,indicator,args):
    if str(indicator).upper() == "SMA":
            sma.sma_buy_sell(script_df,args)
    elif str(indicator).upper() == "MACD":   
            macd.MACD_Strategy(script_df,args)
    elif str(indicator).upper() == "EMA":    
            ema.ema_buy_sell(script_df,args)
    elif str(indicator).upper() == "BOLLINGERBAND":   #*************
            bbands.bbands_buy_sell(script_df ,args)
    elif str(indicator).upper() == "RSI":   
            rsi.rsi_buy_sell(script_df,args)
    elif str(indicator).upper() == "ADX":
            adx.adx_buy_sell(script_df,args)
    elif str(indicator).upper() == "KST":  #KNOW SURE THING INDICATOR
            kst.kst_buy_sell(script_df,args)
    elif str(indicator).upper() == "CCI": #Commodity Channel Index Indicator
            cci.cci_buy_sell(script_df, args)
    elif str(indicator).upper() == "TSI": #True Strength Index 
            tsi.tsi_buy_sell(script_df, args)
    elif str(indicator).upper() == "KC":  # KELTNER CHANNEL
            kc.kc_buy_sell(script_df, args)
    elif str(indicator).upper() == "WILLR": #williams%R   **************
            Willr.willr_buy_sell(script_df,args)
    elif str(indicator).upper() == "RVI": # Relative Vigor Index    *******************
            RVI.rvi_buy_sell(script_df, args)
    elif str(indicator).upper() == "AROON":  #aroon indicator
            aroon.aroon_buy_sell(script_df, args)
    elif str(indicator).upper() == "AO":  # Awesome Oscillator
            ao.ao_buy_sell(script_df,args)
    elif str(indicator).upper() == "ST":  #Super Trend indicator 
            st.st_buy_sell(script_df,args)
    elif str(indicator).upper() == "STOCH": #Stochastic Oscillator 
            stoch.stoch_buy_sell(script_df,args)
    elif str(indicator).upper() == "COPPOCK": #coppock curve 
            coppock.coppock_buy_sell(script_df, args)
    else:
        print("This indicator in not available....")

            