#!/usr/bin/env python3
#New file created
import requests
from bs4 import BeautifulSoup
import easy_requests 

class easySoup(easy_requests.easyRequests):

    def __init__(self):
        self.urlinput = str(input("Enter a valid url for inspection:\n"))


    def cleanCode(self):
        obj = self.check_status()
        print("cleaning code on url {}\n\n ---calling clean code\n\n".format(obj.url))
        soup = BeautifulSoup(obj.text, 'html5lib')
        
        print('soupifying request object, prettifying code--\n')
        
        obj.close()
        return soup

    def writeFile(self):
        x = self.cleanCode()
        print(self.get_information())
        print("gathering infrastructure information for the given url\n")
        self.get_information()
        filename = str(input("Name file you want to create\n"))
        with open(filename+'.html', 'w') as w:
            w.write(x.prettify())
        
        print("created file {} successfully\n".format(filename))
        self.promptScan()

        return
    def scanJson(self):

        x = self.cleanCode()
        print("turning request object into a readable format---")
        print("Scanning and soupifying code--.")
        print(x.prettify())

        self.promptJson()
        return


    def search_tags(self):
        x = self.cleanCode()
        tags = x.find_all(str(input("Enter html tag to parse soup:\n")))
        for t in tags:
            print("{}\n".format(t))
        self.promptSearch()
    def promptSearch(self):
        try:
            choice = int(input("press 1 to scan for more tags\n"))

            if choice == 1:

                
                self.search_tags()
        except: 
            return ValueError("must have entered the wrong keycode\n")


    def promptScan(self):
        try:
            choice = int(input('press 1 to run another scan?\n'))

            if choice == 1:
                self.urlinput = str(input("enter a new url to scan \n"))
                self.writeFile()                
        except:
            return KeyError
          
    def promptJson(self):
        try:
            choice = int(input('press 1 to run another scan?\n'))
            
            if choice == 1:
                self.urlinput = str(input("enter a new url to scan \n"))
                self.scanJson()   

            return 
        except:
            return ValueError
            
            
       



#https://www.alpacainfo.com/