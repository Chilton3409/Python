#!/usr/bin/env python3
# New file created
import requests
import os
import sys
from multiprocessing import Pool
import argparse

class Req():
    def __init__(self):
        self.arguments = argparse.ArgumentParser(description="requests package",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.urlinput = str(input("Enter a valid url for inspection:\n"))


    def clone_url(self):
        request = requests.get(self.urlinput, headers={'Accept': 'Connection'})

        status = request.status_code
        if status != 200:
            print('didnt go through as requested error code {}'.format(status))
        else:
            # only write to file if request is a success.

            print('status code good')
            with open('newclone.html', 'w') as w:
                w.write(request.text)
            request.close()
        return

    def to_json(self):
        request = requests.get(self.urlinput, headers={'Accept': 'Connection'})
        status = request.status_code
        if status != 200:
         print('didnt go through as dialed error code: {}'.format(status))
        else:
            print("request accepted")
            print(request.json())
            
            request.close()
        return
    
    def arg(self):
        self.arguments.add_argument('-t', '--text', action='store_true', help='this will move write the text response to html')
        self.arguments.add_argument('-j', '--json', action='store_true', help="read url in json format")

        args = self.arguments.parse_args()

        if args.text:
            self.clone_url()  

        if args.json:
            self.to_json()  

# Writing to sample.json
def main():
    print("calling main")
    x = Req()
    x.arg()


if __name__ == '__main__':
    with Pool(5) as p:
        p.map(main(), [])
  

      
