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
from concurrent.futures import ThreadPoolExecutor

class RipDevilBot(bot.Bot):

    def __init__(self,key_path,mention_path,last_response_path,media_path):
        super().__init__(key_path,mention_path)
        self.t = twitter.Twitter(self.AUTH,self.API)
        self.last_response_path = last_response_path
        self.mention_path = mention_path
        self.media_path = media_path;
        
    def tweetSearch(self, query):
        lastResponse = filehandling.readFromFile(self.last_response_path)
        tweets = self.t.searchTweet(query, 100,int(lastResponse))
        print('Searching.. ' + str(len(tweets)) + ' found')
        print(tweets)
        
        return tweets #????

    def bob_paint(self):
        while True:
                
                time.sleep(21600)
                c.create_image(1,1,1)
                self.t.tweetWithImage(" ","bob_paint.jpg")
                

    def handle_mentions(self):
        last_mention = 0;
        
        while True:
            new_mentions = self.t.get_new_mentions(self.mention_path)
            print(str(new_mentions))
            if(new_mentions == None):
                pass
            else:
                for mention in new_mentions:
                    self.t.retweet(mention)
                    filehandling.writeToFile(mention,self.mention_path)   
            
            time.sleep(60)


            
    def execute(self):
        executor_list = []
        #self.handle_mentions()
        
        try:
            with ThreadPoolExecutor(max_workers = 5) as executor:
                executor_list.append(executor.submit(self.bob_paint))
                executor_list.append(executor.submit(self.handle_mentions))
            print(executor_list[0].result)

        except KeyboardInterrupt:
            sys.exit(1);
                         
        
