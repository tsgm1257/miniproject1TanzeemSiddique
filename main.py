### INF601 - Advanced Programming in Python
### Tanzeem Siddique
### Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

myTickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

myTickers.sort()
for ticker in myTickers:
    dat = yf.Ticker(ticker)
    hist = dat.history(period="10d")
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    if len(last10days) == 10:
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max() * .05)
        min_price = myarray.min() - (myarray.min() * .05)
        plt.plot(myarray)
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.xlabel("Days Ago")
        plt.ylabel("Closing Price")
        plt.axis((9, 0, min_price, max_price))
        plt.savefig(f"charts/{ticker}.png")
    else:
        print("Do not have 10 days data. Only have {len(last10days)} days data.")

#
#