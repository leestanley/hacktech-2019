import numpy as np
import pandas as pd
import json
import requests

base_url_1 = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='
base_url_2 = '&interval=1min&apikey=RNQUH4LF70UBW4ZM'
def get_ticker_price(ticker):
    url = base_url_1 + ticker + base_url_2
    req = requests.request('GET', url)
    if req.status_code == 200:
        print("Get request successful")
        data = req.json()['Time Series (1min)']
        data = next(iter(data.values()))
        price = data['4. close']
        return price
    else:
        print("Get request unsuccessful")

get_ticker_price("FB")
