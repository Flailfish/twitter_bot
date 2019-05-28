'''
Created on Mar 3, 2017

@author: Derek
'''

import requests

def downloadFile(url,saveAs):
    
    r = requests.get(url)
    with open(saveAs,"wb") as f:
        f.write(r.content)
    