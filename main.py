### INF601 - Advanced Programming in Python
### Tanzeem Siddique
### Mini Project 1

import pprint
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import copy

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

mytickers.sort()
for ticker in mytickers:
    dat = yf.Ticker(ticker)
    hist = dat.history(period="10d")
    # pprint.pprint(dat.info)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    if len(last10days) == 10:
        # maxlist = copy.copy(last10days)
        # maxlist.sort()
        # max_price = maxlist[-1]+10
        # min_price = maxlist[0]-10
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max() * .05)
        min_price = myarray.min() - (myarray.min() * .05)
        plt.plot(myarray)
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.xlabel("Days Ago")
        plt.ylabel("Closing Price")
        plt.axis((9, 0, min_price, max_price))
        plt.show()
    else:
        print("Do not have 10 days data. Only have {len(last10days)} days data.")
        # pprint.pprint(myarray)
    # pprint.pprint(hist['Close'])

# get all stock info


# get historical market date
# hist = dat.history(period="10d")
#
#