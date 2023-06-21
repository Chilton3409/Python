#!/usr/bin/env python3
#New file created
import requests
from multiprocessing import Pool
import argparse
import easy_soup

class Commands(easy_soup.easySoup):
    def __init__(self):
        self.arguments = argparse.ArgumentParser(description="Combining requests and beatiful soup into a basic interactive static code anaylsis tool",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.urlinput = str(input("Enter a valid url for inspection:\n"))


    def arg(self):
        #        self.arguments.add_argument('-t', '--text', action='store_true', help='this will move write the text response to html')
        self.arguments.add_argument('-j', '--json', action='store_true', help="this will prettify the request object into a readable format inside the terminal")

        self.arguments.add_argument('-w', '--write', action='store_true', help="this will clone the given url and write it an html file")
        self.arguments.add_argument('-s', '--search', action='store_true', help="this will search through the url for any tags you want")
        args = self.arguments.parse_args()

        #add custom arguments here
        if args.json:
            self.scanJson()
        if args.write:
            self.writeFile()
        if args.search:
            self.search_tags()

            

def main():
    print('command calling main--')
    x = Commands()
    x.arg()

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(main(), [])
