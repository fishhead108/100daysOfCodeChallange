import pandas as pd
import datetime
import pickle
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from datetime import datetime
import logging
import os
from time import mktime
import sys

import bs4
import feedparser
import requests

import datetime as dt

# from mpl_finance import candlestick_ohlc
# We will look at stock prices over the past year, starting at January 1, 2016
# start = datetime.datetime(2017, 1, 1)
# end = datetime.date.today()
#
# xau = web.DataReader("gold", "google", start, end)
# print(xau.head(n=1000))
# xau["Close"].plot(grid=True)# Plot the adjusted closing price of AAPL
# plt.show()
# pack = pickle.load(open("normalTime.p", "rb"))
# nones = [x for x,y in pack.items() if y == None]
# for pkg in nones:
#     del pack[pkg]
# dct = sorted(pack.values(), key=lambda p: p[1], reverse=True)
# dates = matplotlib.dates.date2num(dct)

packages_time = pickle.load(open("/home/fishhead/local-repos/remote/github.com/100daysOfCodeChallange/code/006/save.p", "rb"))
nones = [x for x,y in packages_time.items() if x == None]
for pkg in nones:
    del packages_time[pkg]

#fulltime = [x.date() for x in packages_time.keys()]
fulltime = [x for x in packages_time.keys()]
fulltime = sorted(fulltime)


#x = [datetime.datetime.strftime(one, '%m/%d/%Y') for one in packages_time]
#x = matplotlib.dates.date2num(fulltime)
y = range(len(fulltime))

#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#plt.plot(x, y)
#plt.gcf().autofmt_xdate()

plt.plot(fulltime, y)
plt.show()
