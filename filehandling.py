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
        
def writeToFile(data,file): 
    try:
        
        f = open(file, 'w') 
        
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
        print('Read from file ' + file + ": "+ str(data))
        f.close() 
        
    return (data);
        
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
        




        