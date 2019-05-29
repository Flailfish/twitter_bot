'''
Created on Feb 27, 2017

@author: Derek

keycrypto.py
handles encrypting and decrypting of keys using AES
encodes the keys in base64 for easier manipulation
'''
import Crypto
from Crypto.Cipher import AES
from Crypto.Util import Padding
import base64
   
def encode(data,key):
        newkey = base64.b64decode(key)
        cipher = AES.new(newkey, AES.MODE_ECB) #create new AES cipher 
        padded_text = Padding.pad(data, 16, 'pkcs7') #add padding if needed
        result = cipher.encrypt(padded_text) #encrypt the padded text
        return base64.b64encode(result); #return a DES encrypted string (base 64 encoded)

def decode(data,key):
        newkey = base64.b64decode(key) #decode the base64 encoded key (was base64 encoded for easier manipulation)
        dater = base64.b64decode(data) #the data is encoded also. (usually the twitter key)
        cipher = AES.new(newkey, AES.MODE_ECB) 
        plaintext = cipher.decrypt(dater) #decrypt the key - get the plaintext
        return Padding.unpad(plaintext, 16, 'pkcs7') #strip off the padding and return the string