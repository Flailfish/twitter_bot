'''
Created on Feb 28, 2017

@author: Derek
'''
import bot
import twitter
import time
import sys
import filehandling
import os
import download
import createimage as c
import random

class RipDevilBot(bot.Bot):
    
    def __init__(self,key_path,mention_path,last_response_path,media_path):
        super().__init__(key_path,mention_path)
        self.t = twitter.Twitter(self.AUTH,self.API)
        self.last_response_path = last_response_path
        self.media_path = media_path;
        
    def tweetSearch(self, query):
        lastResponse = filehandling.readLatestRespondedTo(self.last_response_path)
        tweets = self.t.searchTweet(query, 100,int(lastResponse))
        print('Searching.. ' + str(len(tweets)) + ' found')
        print(tweets)
        
        return tweets
  
            
    def execute(self):
        
        try:
            #self.t.sendTweet("So are mountains.")
            while True:
                time.sleep(21600)
                c.create_image(1,1,1)
                self.t.tweetWithImage(" ","bob.png","4")
                

           
            
                
        except KeyboardInterrupt:
            sys.exit();                           
        