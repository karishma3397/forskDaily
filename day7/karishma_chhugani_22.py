# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:29:08 2018

@author: KC
"""
import oauth2
import urllib.request
import time
import json
url1 = 'https://api.twitter.com/1.1/search/tweets.json'
'''
Consumer Key (API Key)	8PCpsYopUpwLovotBC2dduTRQ
Consumer Secret (API Secret)	BXYWhOPVzN9kJscSMFy0JKY86rYGneXB8TyM38pAGq7iq9onhq
Access Token	2491698797-plmnGcmj39ammb9ttNLleQLo6JUf4GYcJaPfHik
Access Token Secret	V9jdpuyoa8sffYowWf02XJZQYKM39cddx6jkgVsPtgxrS
'''
params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }
consumer = oauth2.Consumer(key="8PCpsYopUpwLovotBC2dduTRQ", secret="BXYWhOPVzN9kJscSMFy0JKY86rYGneXB8TyM38pAGq7iq9onhq")
token = oauth2.Token(key="2491698797-plmnGcmj39ammb9ttNLleQLo6JUf4GYcJaPfHik", secret="V9jdpuyoa8sffYowWf02XJZQYKM39cddx6jkgVsPtgxrS")
params["oauth_consumer_key"] = consumer.key      # VARIABLE AUTHENCATION PARAMETERS

params["oauth_token"] = token.key
params["q"]="jaipur"
req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib.request.Request(url)
data = json.load(urllib.request.urlopen(response))
filename = params["q"]      
f = open(filename + "_File.txt", "w")  # SAVING DATA TO FILE
json.dump(data["statuses"], f)
f.close()
tweets_file = open('jaipur_File.txt', "r")
for line in tweets_file:
    tweet = json.loads(line.strip())
    if 'text' in tweet: # only messages contains 'text' field is a tweet
        print (tweet['id']) # This is the tweet's id
        
        print (tweet['text']) # content of the tweet
                        
 