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
           
            
    def morgan_freeman(self):
        
        freeman_path = r'C:\Users\Derek\My Documents\LiClipse Workspace\twitter\src\freeman.png'
        if(os.path.exists(freeman_path)):
            tweets = self.tweetSearch('morgan%20or%20freeman')
                
            for tweet in tweets:
                time.sleep(600)
            #for url in tweet.entities['urls']:
                url = r'http://twitter.com/' + tweet.user.screen_name + r'/status/' + tweet.id_str
                print(url)
                text = '#morganfreeman\n' + url
                self.t.tweetWithImage(text, freeman_path,self.media_path)
                
        filehandling.writeLatestRespondedTo(tweet.id_str, self.last_response_path)
  
            
    def execute(self):
        try:
           self.t.sendTweet("mate")
            #while(True):
                
                #self.morgan_freeman()
                
        except KeyboardInterrupt:
            sys.exit();                           
        