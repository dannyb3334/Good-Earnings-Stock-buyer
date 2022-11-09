"""
--- pipenv shell
--- pipenv install alpaca_trade_api

"""
'''
  async before functions to run at the same time
'''
import alpaca_trade_api as trade_api
from alpaca_trade_api.rest import TimeFrame 
import numpy as np
import pandas as pd
import time
from datetime import date

current_date = (date.today()).strftime("%Y-%m-%d")
print(current_date)

# authentication and connection details
api_key = 'PK3XYPBZ0SVLX9R1JJWX'
api_secret = 'xBLFA7OXnStxLa36jHCUkHCf786qIPi51srQOgWV'
base_url = 'https://paper-api.alpaca.markets'

# instantiate REST API
api = trade_api.REST(api_key, api_secret, base_url, api_version='v2')

symbol = "APPL"

def is_invested(symbol):
 """Returns True if we own the stock"""

 try:
   rest_api.get_position(symbol)
   return True
 except:
   return False

def buy_regular(symbol, qty):
  api.submit_order(
  symbol=symbol, 
  time_in_force = "day",
  qty=qty, 
  side='buy'
  )

def buy(symbol, qty, limit_price):
  alpaca.submit_order(
    symbol=symbol,
    qty=10,
    type="limit",
    time_in_force="day",
    limit_price=limit_price
  )

while True:
  """ """
  print("")
  print("Checking Price (15 MINUTE DELAY)")
  df = pd.DataFrame()
  market_data = api.get_bars("AAPL", trade_api.TimeFrame(1, trade_api.TimeFrameUnit.Minute)).df.index[:-10]
  print(market_data)
  
  time.sleep(59)