#!/usr/bin/python3

import requests

def main():
    #with open("/home/student/alphavantage.apikey") as apikey:
    #    myapikey = apikey.read()
    mylookup = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=9FCB9TOZMF0T31TY"
    stockdata = requests.get(mylookup)
    lastrefresh = stockdata.json()["Meta Data"]["3. Last Refreshed"]
    print(stockdata.json()["Time Series (5min)"][lastrefresh])
    decodedstockdata = stockdata.json()
    print(decodedstockdata["Time Series (5min)"]["2019-08-20 10:15:00"])


    cryptolookup = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=BTC&to_currency=USD&apikey=9FCB9TOZMF0T31TY"

    crypto = requests.get(cryptolookup)

    cryptojson = crypto.json()

    print(cryptojson['Realtime Currency Exchange Rate']["2. From_Currency Name"])


main()
