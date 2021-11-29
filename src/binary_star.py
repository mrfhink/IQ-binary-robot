import pandas as pd

# TODO:
    # some way to calculate direction of the trend to open position in that direction only.

def ema_cross(df):

    # df['EMA9'] 
    # df['EMA12'] 
    # df['EMA26']
    # df['EMA100']

    ema9_1 = df['EMA9'].iloc[-1]
    ema12_1 = df['EMA12'].iloc[-1] 
    ema26_1 = df['EMA26'].iloc[-1]
    ema9_2 = df['EMA9'].iloc[-2]
    ema12_2 = df['EMA12'].iloc[-2] 
    ema26_2 = df['EMA26'].iloc[-2]
    ema9_3 = df['EMA9'].iloc[-3]
    ema12_3 = df['EMA12'].iloc[-3] 
    ema26_3 = df['EMA26'].iloc[-3]
    cross = 0

    if (ema9_1 > ema12_1 and ema9_1 > ema26_1) and ((ema9_2 < ema12_2 and ema9_2 < ema26_2) or (ema9_3 < ema12_3 and ema9_3 < ema26_3)):
        return  1
    elif (ema9_1 < ema12_1 and ema9_1 < ema26_1) and ((ema9_2 > ema12_2 and ema9_2 > ema26_2) or (ema9_3 > ema12_3 and ema9_3 > ema26_3)):
        return  -1
    else:
        return  0


def adx_cross(df):

    # df['ADX'] 
    # df['minus']
    # df['plus'] 

    plus_1 = df['plus'].iloc[-1]
    minus_1 = df['minus'].iloc[-1] 
    adx_1 = df['ADX'].iloc[-1]
    
    cross = 0

    if plus_1 > minus_1 and plus_1 > adx_1:
        return  1
    elif minus_1 > plus_1 and minus_1 > adx_1:
        return  -1
    else:
        return 0


def macd_cross(df):

    # df['MACD'] 
    # df['MACD_signal']

    cross = 0

    if df['MACD'].iloc[-1] > 0 and df['MACD'].iloc[-3]:
        return  1
    elif df['MACD'].iloc[-1] < 0 and df['MACD'].iloc[-3]:
        return  -1
    else:
        return  0


