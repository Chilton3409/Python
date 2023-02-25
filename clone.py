#!/usr/bin/env python3
#New file created
from multiprocessing import Pool
import os
import sys
from wsgiref import headers
import requests
from json_uses import dump, write



#!/usr/bin/env python3
#New file created
from wsgiref import headers
import requests
import sys
import json 


"""
response = requests.get('https://tranquil-fjord-83920.herokuapp.com/hemp/',
                        params={'q': 'Chapter 1'},
                        headers={'Accept': 'Connection'}

                        )

json_response = response.json()
print(json_response)

"""

urlinput = sys.argv[1]
def clone_url(urlinput=str):
    request = requests.get(urlinput, headers={'Accept': 'Connection'})

    status = request.status_code
    if status != 200:
        print('didnt go through as requested error code {}'.format(status))
    else:
        #only write to file if request is a success.
        
        print('status code good')
        with open('newclone.html', 'w') as w:
            w.write(request.text)


    
   
    request.close()
    return
    
# Writing to sample.json

if __name__ == '__main__':
    with Pool(5) as p:

        p.map(clone_url,[urlinput])
    



