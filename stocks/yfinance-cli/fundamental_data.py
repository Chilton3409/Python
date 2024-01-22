#!/usr/bin/env python3
#New file created
import yfinance as yf

dhr = yf.Ticker('AWIN')

print(dhr.get_financials())
print(dhr.get_balancesheet())
print(dhr.get_history_metadata())
#print(dhr.get_news())
#print(dhr.get_cash_flow())