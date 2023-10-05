#!/usr/bin/env python3
#New file created
import requests

class easyRequests():

    def __init__(self):
        self.urlinput = str(input("Enter a valid url for inspection:\n"))
        
    def check_status(self):
        #need to return a bool or a request object here
        request = requests.get(self.urlinput, headers={'Accept': 'Connection'})
        if request.status_code == 200:

            print("Successfully pinging url {} with a status code {}\n".format(request.url, request.status_code))
            return request
        else:
            print("could not ping url {}, status code {}\n".format(request.url, request.status_code))
            return request
  
    def get_information(self):
        x = self.check_status()
        cookies = x.cookies
        print("gathered cookie {} on url {}.".format(cookies, x.url))
        headers = x.headers
        print("here on the headers for url: {}, : {}".format(x.url, headers))
        #add writing to a file later on 
        return x




    

        
    
    
            


