'''
Created on Feb 28, 2017

@author: Derek

'''
import tweepy
import keycrypto
import filehandling


class Bot:
    
    def __init__(self,key_path,mention_path):
        self.keyPath = key_path
        self.mentionPath = mention_path 
        self.keys = filehandling.readFromFile(key_path)
        print(self.keys)
        self.cSecret = keycrypto.decode(self.keys[0],self.keys[4]) 
        self.cToken = keycrypto.decode(self.keys[1],self.keys[4])
        self.aToken = keycrypto.decode(self.keys[2],self.keys[4])
        self.aSecret = keycrypto.decode(self.keys[3],self.keys[4])
        self.AUTH = tweepy.OAuthHandler(self.cToken,self.cSecret); 
        self.AUTH.set_access_token(self.aToken, self.aSecret);
        self.API = tweepy.API(self.AUTH,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        
    def execute(self):
        pass
            