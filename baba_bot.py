#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:49:47 2018

@author: ich
"""
INTERVAL = 60


import urllib.request, json, tweepy, datetime, re, time
        
#get private keys for the twittter account from module
from keys import keys
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
    
#login to twitter-app to be abled to call twiter's API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitterAPI = tweepy.API(auth)
 
def checkReplies(origTweetID):
    allReplies = twitterAPI.search(q="#servusbaba")
    for reply in allReplies:
         if (reply.in_reply_to_status_id == origTweetID):
             return(True)
       
def addSpace(text):
    "Adds spaces when a camelCase is found"
    while re.match(r".*[a-z][A-Z].*" , text):
        span = (re.search(r"[a-z][A-Z]" , text).span())
        location = ((span[0])+1)
        text = (text[:location] + ' ' + text[location:])
    return(text)
    
def tweetSalute(user,replyToID):
    "Calls the Twitter API to post a reply with a random quote, also does some repairwork if a space is missing"
    #get the source material as json from the quotesalute webservice
    jsonsource = "https://correspsearch.net/quotesalute/abfrage.xql"
    jsonsalute = urllib.request.urlopen(jsonsource)
    fullsalute = json.loads(jsonsalute.read())
    salute = fullsalute['quote']
    #check for missing spaces (=camelCase) with regex
    if re.match(r".*[a-z][A-Z].*" , salute ):
        salute = addSpace(salute)
    #send the reply
    twitterAPI.update_status("{} @{} #servusbaba".format(salute,user) , in_reply_to_status_id = replyToID)
    print("{} @{}".format(salute,user))
        
while True:
    #find all mentions and update the lastChecked timer
    allMentions = twitterAPI.search(q="@servusbaba")
    for mention in allMentions:
        #check if mention was already replied to
        if not(checkReplies(mention.id)):
            print(mention.text)
            fromUser = mention.user.screen_name
            mentionID = mention.id
            tweetSalute(fromUser,mentionID)
        else:
            print("old mention found (from @baba{})".format(mention.user.screen_name))
    
    time.sleep(INTERVAL)