import time
import numpy as np
import pandas as pd
import ta as tafin
from finta import TA

def load_goals(iq):
    '''
    Gets open instruments and their profit from IQ
    '''
    
    profits_from_iq =iq.get_all_profit()
    assets_from_iq =iq.get_all_open_time()

    inst = {i:profits_from_iq[i]['turbo'] for i in assets_from_iq['turbo'] if assets_from_iq['turbo'][i]['open']==True}


    return inst


def rename_data(candles):
    '''
    Renames some df columns in order to calculate some indicators

    '''

    df = pd.DataFrame(candles).rename(columns={'max':'high', 'min':'low'})
    return df


def get_indicators(df, period_adx=14,
                   period_fast=12,
                   period_slow=26,
                   window_size=5,
                   poly_order=3,
                   signal=9):
    '''
    Calculates and returns the following indicators from the df given:

        ADX:
            period = 14
        EMAs:
            means 9, 12, 26, 100
        MACD:
            period_fast = 12
            period_slow = 26
            signal = 9

    '''

    # ADX Indicator
    adx = tafin.trend.ADXIndicator(
        df['high'], df['low'], df['close'], period_adx)
    df['ADX'] = tafin.trend.ADXIndicator.adx(adx)
    df['minus'] = tafin.trend.ADXIndicator.adx_neg(adx)
    df['plus'] = tafin.trend.ADXIndicator.adx_pos(adx)

    # EMAs 9-12-26-100
    df['EMA9'] = TA.EMA(df, 9)
    df['EMA12'] = TA.EMA(df, 12)
    df['EMA26'] = TA.EMA(df, 26)

    # MACD
    df['MACD'] = TA.MACD(df, period_fast, period_slow, signal)['MACD']
    df['MACD_signal'] = TA.MACD(df, period_fast, period_slow, signal)['SIGNAL']
    
    return df

# Logging

def login(IQ_api, balance_mode="PRACTICE"):
    """
    Logs in to the broker. 

    Requires IQ object and balance mode (default PRACTICE)
    """

    print('Please enter your login information...')
    email = str(input('Email: '))
    pwd = str(input('Password: '))
    try:
        iq = IQ_api(email, pwd)
        check, reason = iq.connect()
        if check:
            print('Logged in...')
            print('Balance mode: ', balance_mode)
            iq.change_balance(balance_mode)
            print('Balance: ', iq.get_balance())
    except:
        print('Failed to login')
    return iq

