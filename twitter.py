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
user = '@ismynanTwitch'
rate_limit_errors = 0;

class Twitter:
    
    def __init__(self,auth,api):
        self.auth = auth
        self.api = api
        

    def readPublicTweets(self): 
        publicTweets = self.api.home_timeline() 
        for publicTweet in publicTweets:
            print(publicTweet.text) 
        

    def sendTweetTo(self,handle,text): 
    
        try:
            tweet = self.api.update_status(handle + " " + text) 
            tweetId = tweet.id 
            print(tweet)        
        except tweepy.TweepError:
                
                print('Error sending tweet') 
        
                
                
    def sendTweet(self,text): 
    
        try:
            tweet = self.api.update_status(text) 
            tweetId = tweet.id 
            print(tweet)        
        except tweepy.TweepError:
                raise tweepy.TweepError
                print('Error sending tweet') 
                
    def uploadImage(self,path,savePath):
        #try:
            images = (path)
            media = [self.api.media_upload(images).media_id]
            filehandling.appendToFile(media,savePath)
            print(media)
            return media
        #except tweepy.TweepError:
        
                
    def tweetWithImage(self,text,imagePath,savePath): 
    
        #try:
            media_id = self.uploadImage(imagePath, savePath)
            #media_id = filehandling.readFromFile(savePath)
            print(media_id)
            #print(media_id[1])
            tweet = self.api.update_status(status = text,media_ids = media_id) 
            print(tweet)        
        #except tweepy.TweepError:
            #print('Error sending tweet') #handle errors
        
                
        
    def favouriteTweet(self,fTweetId):
        try:
            self.api.create_favorite(fTweetId); #favourite the tweet given the tweetId
        except: tweepy.TweepError
        

    def retweet(self,tId):
    
        try:
            self.api.retweet(tId); #retweet tweet id
        except tweepy.TweepError:
            print('Unable to retweet..') #handle errors
        
    def sendCommand(self,com, arg): #do actions based on the command sent - more will be added
        if (com.lower()).__eq__('retweet'): #if command is 'retweet' then retweet the tweet
            self.retweet(arg) #arg is the command arguments (tweet id in this case)
    
#handle cmd arg     
    def parseCommand(self,command): #parses the command
        st = command.split(' ', 3) # the tweet is split into 3 sections - shown above
        cmd = st[1] #index 1 is the command
        args = st[2] #index 2 is the arguments. index 0 is the handle of sender - already accounted for

        self.sendCommand(cmd,args) #run command
    
        
    def mentionSearch(self): #poll mentions.. search for new mentions
        lastMention = filehandling.readLastMention() #read last mention from file
        try:
            #while True:
            
                mentions = self.api.mentions_timeline(since_id = lastMention) #grab the latest mention not responded to
                for mention in mentions:
                    print(mention.text)
                    print(mention.user.screen_name)
                    if ((mention.user.screen_name).__eq__('ismynanTwitch')): #only respond to this user
                        if lastMention == mention.id: #if the latest mention responded to = the latest mention
                            pass #there are no new mentions.. so do nothing
                            print('no new mentions')
                        elif(lastMention != (mention.id)): #if the last mention is not the same as the latest
                                print(mention.text) #there are mentions we haven't responded to.. so respond to them
                                self.parseCommand(mention.text) #grab and parse command from tweet
                                lastMention = mention.id #lastMention = the tweet we just responded to
                                print(lastMention)
                                print(mention.id)
                                filehandling.writeLastMentionToFile(lastMention) #write last mention to file now
                                #just in case the execution fails for some reason
                        
                    time.sleep(15)              #wait for 15 seconds as not to exceed twitters rate limit         
         
        except tweepy.RateLimitError: # handle errors such as rate limiting errors (eventually)
            print("Rate limit exceeded.. waiting 15 minutes.")
            rate_limit_errors+= 1
            print('Rate limiting errors: ' + rate_limit_errors)
            time.sleep(900) #sleep for 15 minutes
            self.mentionSearch()

    def searchTweet(self,query,number,age):
        if age > 0:
            tweet_list = self.api.search(q = query, count = number, include_entities = True,result_type = 'mixed', since_id = age)
        elif age == 0:
            tweet_list = self.api.search(q = query, count = number, include_entities = True,result_type = 'mixed')   
        return tweet_list;
            
    