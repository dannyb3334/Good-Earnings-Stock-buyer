'''
--- pipenv shell
--- pipenv install alpaca_trade_api

'''
'''
  async before functions to run at the same time
'''
import alpaca_trade_api as trade_api
from scrapper import *

# authentication and connection details
api_key = 'PKEUXZLRW917250UT5GO'
api_secret = '4VArCw0af3A1PfcvQhbqy5VUWeJltmPw7Ic97Ivx'
base_url = 'https://paper-api.alpaca.markets'
i = 0
# instantiate REST API
try: 
  api = trade_api.REST(api_key, api_secret, base_url, api_version='v2')
  print("...Connected to Paper Account...")
except:
  print("...Connection Error, Verify API Keys...")

def buy(symbol, qty):
  try:
    api.submit_order(
    side= 'buy',
    symbol= symbol,
    #type= 'trailing_stop',
    #trail_percent= 1,
    qty= qty,
    time_in_force= 'gtc'
    )
  except: 
    print(symbol + ' error')

while True:
  symbols = get_good_reports(i)
  if symbols == 'none':
    i = i + 1
    continue
  if symbols == 'end':
    browser.close()
    quit()
  for sym in symbols:
    buy(sym, 10)
  i = i + 1
  
  