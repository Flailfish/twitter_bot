'''
Created on Feb 27, 2017

@author: Derek

filehandling.py
This module is meant for doing the file handling
eg. writing the keys to a file, writing the last mention to a file, and reading them
'''


def appendToFile(data,file): 
    try:
        
        f = open(file, 'a') 
        
    except IOError: 
        print("Could not write to file " + file);
    else: 
        f.write(str(data) + "\n") 
        print('Data: ' + str(data) + ' written to ' + file) 
        f.close() 
        
def readFromFile(file):
    
    try:
       f = open(file,'r') 
    except IOError: 
        print("Could not read from file: " + file)
    else:
        data = []
        data = f.read().splitlines() 
        print('Read from file ' + file)
        f.close() 
        
    return (data);

def writeLastMentionToFile(last,mention_file): 
    try:
        
        last_mention_file = open(mention_file, 'w') 
        
    except IOError: 
        print("Could not write to file " + mention_file);
    else: 
        last_mention_file.write(str(last)) 
        print('Mention: ' + str(last) + ' written to ' + mention_file) 
        last_mention_file.close() 
        
def readLastMention(mention_file):
    
    try:
        last_mention_file = open(mention_file,'r') 
    except IOError: 
        print("Could not read from file: " + mention_file)
    else:
        last_mention = last_mention_file.read()
        print('Read: ' + last_mention + ' from file ' + mention_file)
        last_mention_file.close() 
        
    return int(last_mention);
        
def writeKeyToFile(key,keyPath): # at some point add the ability to clear the file first
    try: 
        contents = key.decode('utf-8') + '\n' #convert the key(byte) to string (utf-8 encoding)
        key_file = open(keyPath,'a') 
    except IOError: 
        print('Could not write key to file ' + keyPath + ' (' + contents + ')')
    else:
        key_file.write(contents) 
        print(contents + ' written to ' + keyPath) 
        key_file.close() 
        
def readKeysFromFile(keyPath):
    try:
        keys = [] 
        key_file = open(keyPath,'r') 
    except IOError: 
        print('Could not read from file: ' + keyPath)
    else:
        
        keys = key_file.read().splitlines() #jam each line into a list
        print('Read keys from file ' + keyPath) 
        key_file.close() 
    return keys #return a list of keys

def writeLatestRespondedTo(last,respond_path):
    try:
        respond_file = open(respond_path,'w')
    except IOError:
        print('Error writng to file ' + respond_path)
    else:
        respond_file.write(last)
        print("Wrote latest response " + last + " to " + respond_path)
        respond_file.close()
        
def readLatestRespondedTo(respond_path):
    try:
        respond_file = open(respond_path,'r')
    except IOError:
        print('Error writng to file ' + respond_path)
    else:
        lastResponse = respond_file.read()
        print("Read latest response " + lastResponse + " from " + respond_path)
        respond_file.close()
        return lastResponse


        