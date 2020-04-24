'''
Created on Feb 26, 2017

@author: Derek

twitter.py
Handles twitter authentication, receiving/sending tweets, dms,etc
'''
import tweepy
import time
import filehandling
import keycrypto
user = '--------'
rate_limit_errors = 0;

class Twitter:
    
    def __init__(self,auth,api):
        self.auth = auth
        self.api = api
        
    def readPublicTweets(self): 
        publicTweets = self.api.home_timeline() 
        for publicTweet in publicTweets:
            print(publicTweet.text)             
                
    def sendTweet(self,text): 
    
        try:
            tweet = self.api.update_status(text) 
            tweetId = tweet.id 
            print(tweet)        
        except tweepy.TweepError as e:
                print(e.response.text) 
                
    def uploadImage(self,path):
        try:
            images = (path)
            media = [self.api.media_upload(images).media_id]
            print(media)
            return media
        except tweepy.TweepError as e:
            print(e.response.text)
        
                
    def tweetWithImage(self,text,imagePath): 
    
        try:
            media_id = self.uploadImage(imagePath)
            tweet = self.api.update_status(status = text, media_ids = media_id) 
            print(tweet)        
        except tweepy.TweepError as ex:
            print(ex.response.text) 
             
    def favouriteTweet(self,fTweetId):
        try:
            self.api.create_favorite(fTweetId); #favourite the tweet given the tweetId
        except: tweepy.TweepError
        

    def retweet(self,tId):
    
        try:
            self.api.retweet(tId); #retweet tweet id
        except tweepy.TweepError:
            print('Unable to retweet..') #handle errors 


        
    def get_new_mentions(self,mention_file): #poll mentions.. search for new mentions
        
        known_mentions = filehandling.readFromFile(mention_file) #read last mention from file check if it's the most recent
        print('hhh')
        #we need to store the most recent mention in a file just incase the bot crashes - otherwise it will respond to mentions multiple times.
        try:
            new_mentions = []
            mentions = self.api.mentions_timeline(since_id = int(known_mentions[0]))
            if (len(mentions) > 0):
                
                for mention in mentions:
                    new_mentions.append(mention.id)
                return new_mentions
                    
            else:
                print("no new mentions")
                return None

        except (tweepy.RateLimitError, Exception) as e: # handle errors such as rate limiting errors (eventually) but probably not
            print(e)
            print("Rate limit exceeded.. waiting 15 minutes.")
            
            time.sleep(900) #sleep for 15 minutes
            

    def searchTweet(self,query,number,age): #search for tweets that match a specified search query - tweet age can be specified and # of tweets
        if age > 0:
            tweet_list = self.api.search(q = query, count = number, include_entities = True,result_type = 'mixed', since_id = age)
        elif age == 0:
            tweet_list = self.api.search(q = query, count = number, include_entities = True,result_type = 'mixed')   
        return tweet_list;
            
    
