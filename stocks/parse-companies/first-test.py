#!/usr/bin/env python3
#New file created
from multiprocessing import Pool
import argparse
import yfinance as yf

class Company():
    def __init__(self):
        self.arguments = argparse.ArgumentParser(description="Search through a companies financials by entering their ticker symbol")
        self.ticker = input("Enter a Company's stock symbol to start inspecting their financials\n").upper()
        self.my_symbols = []
        
    def prompt(self):
        try:
            choice = int(input("press 1 to add this symbol to my symbols\n"))

            if choice == 1:
                self.my_symbols.append(self.ticker)
                print(self.my_symbols)
                
        except:
            return KeyError

    def get_basic_info(self):
        sym = yf.Ticker(str(self.ticker))
        print(sym.fast_info)
        print(
            'last price: ',sym.fast_info['lastPrice'], 'last volume: ', sym.fast_info['lastVolume'],
            'last year high:', sym.fast_info['yearHigh'], 'last year low:', sym.fast_info['yearLow']
            )
        print('year change:', sym.fast_info['yearChange'], 'two hundred day average:', sym.fast_info['twoHundredDayAverage'])
        self.prompt()      
        
    def get_financials(self):
        sym = yf.Ticker(str(self.ticker))
        print('-------------printing basic info')
        print('--------printing financial data------')
        print(sym.get_financials(pretty=True))
        print('--------------now printing income statement')
        print(sym.get_income_stmt())
          
    def get_balanceSheet(self):
        sym = yf.Ticker(str(self.ticker))
        print('printing company balance sheet')
        print(sym.get_balancesheet(pretty=True))
    
    def get_historical_metadata(self):
        sym = yf.Ticker(str(self.ticker))
        print('gathering company historical metadata')
        print(sym.get_history_metadata())
        #todos---add inputs for intervals and periods

    def get_company_news(self):
        sym = yf.Ticker(str(self.ticker))
        print(sym.get_news())
        #todo's filter out content to only print out

    def get_company_cash_flow(self):
        sym = yf.Ticker(str(self.ticker))
        print(sym.get_cash_flow(pretty=True))

    def arg(self):
        self.arguments.add_argument('-f', '--financials', action='store_true', help='this will gather a companies financials'),
        self.arguments.add_argument('-b', '--balancesheet', action='store_true', help='retrieve the balance sheet for the company you are searching for')
        self.arguments.add_argument('-m', '--history', action='store_true', help='this will retrieve the companies historical metadata')
        self.arguments.add_argument('-n', '--news', action='store_true', help='this will gather news on the currently tracked company')
        self.arguments.add_argument('-c', '--cashflow', action='store_true', help='this will gather the currently tracked companies cash flow')
        self.arguments.add_argument('-i', '--info', action='store_true', help='gather basic information about the currently tracked company')

        args = self.arguments.parse_args()

        if args.financials:
            self.get_financials()

        if args.balancesheet:
            self.get_balanceSheet()

        if args.history:
            self.get_historical_metadata()

        if args.news:
            self.get_company_news()

        if args.cashflow:
            self.get_company_cash_flow()

        if args.info:
            self.get_basic_info()

def main():
    print("-----calling main, gathering company financial data")
    x = Company()
    x.arg()

if __name__=='__main__':
    with Pool(5) as p:
        p.map(main(), [])
