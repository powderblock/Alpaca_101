import alpaca_trade_api as tradeapi
import time
import pandas as pd

#current_time = pd.Timestamp().isoformat()
#print(current_time)

key = "<YOUR KEY HERE>"
sec = "<YOUR SECRET HERE>"

#API endpoint URL
url = "https://paper-api.alpaca.markets"

#api_version v2 refers to the version that we'll use
#very important for the documentation
api = tradeapi.REST(key, sec, url, api_version='v2')

#Init our account var
account = api.get_account()

def get_num_shares(stock):
    all_pos = api.list_positions()
    i = 0
    for i in range(len(all_pos)):
        if stock == all_pos[i].symbol:
            return all_pos[i].qty
    #If we don't find it in all_pos
    return 0
print(api.list_orders(status="filled"))
