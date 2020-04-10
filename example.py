import alpaca_trade_api as tradeapi
import time

key = "<YOUR KEY HERE>"
sec = "<YOUR SECRET HERE>"

#API endpoint URL
url = "https://paper-api.alpaca.markets"

#api_version v2 refers to the version that we'll use
#very important for the documentation
api = tradeapi.REST(key, sec, url, api_version='v2')

#Init our account var
account = api.get_account()

print(account.status)
