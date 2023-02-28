#!/usr/bin/env python3
#New file created
import os
import sys  
import argparse
from multiprocessing import Pool

class Parse():
    def __init__(self):
        self.arguments = argparse.ArgumentParser(description="Os moving files around", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    def copy(self):
        print("copy function")
        
        pass
    def read(self):
        with open(str(input("enter a file to read\n")), 'r') as new:
           data = new.read()
           return data
        
    def split(self):
        with open(str(input("enter a file to split\n")), 'r') as f:

            data = f.readlines()
            for line in data:
                word = line.split()
                return word
    def read_csv(self):
        with open(str(input("enter filepath")), 'w') as csv_file:
            for line in csv_file:
                print(line)
            
        

    def move():
        pass

    def arg(self):
        self.arguments.add_argument('-c', '--copy', action='store_true', help="this will copy a file")
        self.arguments.add_argument('-m', '--move', action='store_true', help="this will move a file")
        self.arguments.add_argument('-l', '--listfile', action='store_true', help="this will move a file")
        self.arguments.add_argument('-s', '--split', action='store_true', help="this split words in a textfile into a list")
        args = self.arguments.parse_args()
        
        if args.copy:
            print(self.copy())

        if args.move:
            print('calling move')

        if args.listfile:
            print(self.read())
        if args.split:
            print(self.split())

def main():
    print("calling main")
    x = Parse()
    x.arg()

if __name__ =='__main__':
    main()


         
    
        
    
