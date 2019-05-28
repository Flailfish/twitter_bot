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
keys = filehandling.readKeysFromFile()
rate_limit_errors = 0

cSecret = keycrypto.decrypt(keys[0]) 
cToken = keycrypto.decrypt(keys[1])
aToken = keycrypto.decrypt(keys[2])
aSecret = keycrypto.decrypt(keys[3])
    
auth = tweepy.OAuthHandler(cToken,cSecret); 
auth.set_access_token(aToken, aSecret);
api = tweepy.API(auth) 

def readPublicTweets(): 
    publicTweets = api.home_timeline() 
    for publicTweet in publicTweets:
        print(publicTweet.text) 
        

def sendTweet(handle,text): 
    
    try:
        tweet = api.update_status(handle + " " + text) 
        tweetId = tweet.id 
        print(tweet)        
    except tweepy.TweepError:
        print('Error sending tweet')
        
    favouriteTweet(tweetId); 
        
def favouriteTweet(fTweetId):
    try:
        api.create_favorite(fTweetId); #favourite the tweet given the tweetId
    except: tweepy.TweepError
        #print('Unable to favourite tweet')

def retweet(tId):
    
    try:
        api.retweet(tId); #retweet tweet id
    except tweepy.TweepError:
        print('Unable to retweet..') #handle errors
        
def sendCommand(com, arg): #do actions based on the command sent - more will be added
    if (com.lower()).__eq__('retweet'): #if command is 'retweet' then retweet the tweet
        retweet(arg) #arg is the command arguments (tweet id in this case)
    
#handle cmd arg     
def parseCommand(command): #parses the command
    st = command.split(' ', 3) # the tweet is split into 3 sections - shown above
    cmd = st[1] #index 1 is the command
    args = st[2] #index 2 is the arguments. index 0 is the handle of sender - already accounted for

    sendCommand(cmd,args) #run command
    
        
def mentionSearch(): #poll mentions.. search for new mentions
    lastMention = filehandling.readLastMention() #read last mention from file
    try:
        while True:
            
            mentions = api.mentions_timeline(since_id = lastMention) #grab the latest mention not responded to
            for mention in mentions:
                print(mention.text)
                print(mention.user.screen_name)
                if ((mention.user.screen_name).__eq__('ismynanTwitch')): #only respond to this user
                    if lastMention == mention.id: #if the latest mention responded to = the latest mention
                        pass #there are no new mentions.. so do nothing
                        print('no new mentions')
                    elif(lastMention != (mention.id)): #if the last mention is not the same as the latest
                        print(mention.text) #there are mentions we haven't responded to.. so respond to them
                        parseCommand(mention.text) #grab and parse command from tweet
                        lastMention = mention.id #lastMention = the tweet we just responded to
                        print(lastMention)
                        print(mention.id)
                        filehandling.writeLastMentionToFile(lastMention) #write last mention to file now
                        #just in case the execution fails for some reason
                        
            time.sleep(15)   #wait for 15 seconds as not to exceed twitters rate limit         
         
    except KeyboardInterrupt: #allow for user interrupt by Ctrl-C
        pass
    except tweepy.RateLimitError: # handle errors such as rate limiting errors (eventually)
        print("Rate limit exceeded.. waiting 15 minutes.")
        #rate_limit_errors++
        print('Rate limiting errors: ' + rate_limit_errors)
        time.sleep(900) #sleep for 15 minutes
        mentionSearch()
    
mentionSearch() 
