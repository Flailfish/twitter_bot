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
        
    
    rdb = DevilBot.RipDevilBot(r'C:\Users\Derek\Documents\LiClipse Workspace\twitter\src\fred.dat',r'C:\Users\Derek\Documents\LiClipse Workspace\twitter\src\devillastmention.dat',r'C:\Users\Derek\Documents\LiClipse Workspace\twitter\src\lastresponse.dat',r'C:\Users\Derek\Documents\LiClipse Workspace\twitter\src\devilmedia.dat')
    rdb.execute()
    
    
main()