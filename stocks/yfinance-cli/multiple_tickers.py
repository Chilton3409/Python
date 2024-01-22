#!/usr/bin/env python3
#New file created
import yfinance as yf

data = yf.download(['INPX','AWIN', 'FOXO', 'ABVC','LQR'], period='1mo')
print(data.head())

