#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:49:47 2018

@author: ich
"""
import urllib.request, json, tweepy, datetime, re

#get private keys for the twittter account from module
from keys import keys
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

#login to twitter-app to be able to call twiter's API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitterAPI = tweepy.API(auth)

def addSpace(text):
    "Adds spaces when a camelCase is found"
    while re.match(r".*[a-z][A-Z].*" , text):
        span = (re.search(r"[a-z][A-Z]" , text).span())
        location = ((span[0])+1)
        text = (text[:location] + ' ' + text[location:])
    return(text)

def tweetSalute(user):
    "Calls the Twitter API to post a status update with a random quote, also does some repairwork if a spaces is missing"
    jsonsource = "https://correspsearch.net/quotesalute/abfrage.xql"
    jsonsalute = urllib.request.urlopen(jsonsource)
    fullsalute = json.loads(jsonsalute.read())
    salute = fullsalute['quote']

    #check for missing spaces (=camelCase) with regex
    if re.match(r".*[a-z][A-Z].*" , salute ):
        salute = addSpace(salute)
    
    twitterAPI.update_status("{} @{}".format(salute,user))
    print("{} @{}".format(salute,user))
    
#find all mentions and update the lastChecked timer
allMentions = twitterAPI.search(q="@servusbaba")
lastChecked = datetime.datetime.now()

#weed out the mentions that have already been seen
for mention in allMentions:
    print(mention.text)
    print(mention.created_at)
    print(lastChecked)
    if mention.created_at < lastChecked:
        fromUser = mention.user.screen_name
        tweetSalute(fromUser)