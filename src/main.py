import time
import sys
import iq
from iqoptionapi.stable_api import IQ_Option
import binary_star
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

investing = 1
CANDLE_TIME = 60
CANDLE_NUMBER = 60

MAX_INSTRUMENTS = 5

ema_cross = 0
macd_cross = 0
adx_cross = 0

api_iq = iq.login(IQ_Option, "PRACTICE")
assets = iq.load_goals(api_iq)

while True:
    while int(time.localtime().tm_sec % 60) < 2:
        start = time.process_time()
        print('\n')
        print('Getting indicators\n')
        for asset in assets.keys():

            goal_asset = iq.rename_data(api_iq.get_candles(
                asset, CANDLE_TIME, CANDLE_NUMBER, time.time()))
            
            target_df = iq.get_indicators(goal_asset)
            asset_trend = binary_star.data_trend(goal_asset, CANDLE_NUMBER, asset)

            ema_cross = binary_star.ema_cross(target_df)
            macd_cross = binary_star.macd_cross(target_df)
            adx_cross = binary_star.adx_cross(target_df)

            # Strategy Call
            if ema_cross == 1 and macd_cross == 1 and adx_cross == 1 and asset_trend == 1:
                ID =api_iq.buy(1, asset, 'call', 3)
                print('Buying: ', asset, ' ID: ', ID)

            # Strategy Put
            if ema_cross == -1 and macd_cross == -1 and adx_cross == -1 and asset_trend == -1:
                ID = api_iq.buy(1, asset, 'put', 3)
                print('Selling: ', asset, ' ID: ', ID)
        
        print('\n')
        print('Getting profits\n')
        
        # Setting goals by profit
        assets = iq.load_goals(api_iq)
        timeToSleep = 60 - time.localtime().tm_sec - 1
        print('Waiting next candles ', timeToSleep, " seconds.\n")
        time.sleep(timeToSleep)
        print('')
