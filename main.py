### INF601 - Advanced Programming in Python
### Tanzeem Siddique
### Mini Project 1

import pprint
import yfinance as yf

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

mydata = {}

mytickers.sort()
for ticker in mytickers:
    dat = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                      'dayHigh': dat.info["dayHigh"]
                      }
    pprint.pprint(mydata)

# dat = yf.Ticker("AAPL")

# get all stock info
# pprint.pprint(dat.info)

# get historical market date
# hist = dat.history(period="10d")
#
# pprint.pprint(hist)