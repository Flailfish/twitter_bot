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
        
    
    rdb = DevilBot.RipDevilBot(r'fred.dat',r'devillastmention.dat',r'lastresponse.dat',r'devilmedia.dat')
    rdb.execute()
    
    
main()
