#!/usr/bin/env python3
#New file created
import yfinance as yf
import datetime

obj = yf.Ticker('AWIN')
data = obj.history(interval='1m', start='2023-11-01',end='2023-11-03')
print(data.head())

