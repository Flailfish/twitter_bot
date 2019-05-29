'''
Created on Feb 28, 2017

@author: Derek
'''

import DevilBot
import bot
import twitter
import filehandling
import keycrypto


def main():     
        
    
    rdb = DevilBot.RipDevilBot(r'C:\Users\Derek\Source\repos\twitter_bot\fred.dat',r'C:\Users\Derek\Source\repos\twitter_bot\devillastmention.dat',r'C:\Users\Derek\Source\repos\twitter_bot\lastresponse.dat',r'C:\Users\Derek\Source\repos\twitter_bot\devilmedia.dat')
    rdb.execute()
    
    
main()