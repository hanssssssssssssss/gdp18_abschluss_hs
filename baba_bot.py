#python3.7
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:49:47 2018

@author: Hans Straile
"""
import json
import re
import time
import urllib.request
import tweepy

#get private keys for the twittter account
from keys import keys
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

#Set seconds of sleep before checking for new messages. Twitter API allows for 100 calls per minute
INTERVAL = 60

#login to twitter-app to call twiter's API
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
TWITTER_API = tweepy.API(AUTH)

def check_replies(origtweet_id):
    "checks if any tweet with the signature hashtag is a reply to the orig. tweet"
    all_replies = TWITTER_API.search(q="#servusbaba")
    return True in (reply.in_reply_to_status_id == origtweet_id for reply in all_replies)

def add_space(text):
    "Adds spaces where a camelCase is found"
    while re.match(r".*[a-z][A-Z].*", text):
        #find the location where the string matches the regex
        span = (re.search(r"[a-z][A-Z]", text).span())
        location = ((span[0])+1)
        #add spce inbetween
        text = (text[:location] + ' ' + text[location:])
    return text

def tweet_salute(user, replyto_id):
    "tweets a reply with a random quote, initiates add_space if a space is missing"
    #get the source material as json from the quotesalute webservice
    jsonsource = "https://correspsearch.net/quotesalute/abfrage.xql"
    jsonsalute = urllib.request.urlopen(jsonsource)
    fullsalute = json.loads(jsonsalute.read())
    salute = fullsalute['quote']
    #check for missing spaces (CamelCase) with regex
    if re.match(r".*[a-z][A-Z].*", salute):
        salute = add_space(salute)
    #send the reply
    TWITTER_API.update_status(
        "{} @{} #servusbaba".format(salute, user), in_reply_to_status_id=replyto_id)
    print("{} @{}".format(salute, user))

while True:
    #find all mentions and check if the bot already replied
    ALL_MENTIONS = TWITTER_API.search(q="@servusbaba")
    if not ALL_MENTIONS:
        print("no mentions found")
    else:
        for mention in ALL_MENTIONS:
            #check if mention was already replied to
            if not check_replies(mention.id):
                print(mention.text)
                fromUser = mention.user.screen_name
                tweet_salute(fromUser, mention.id)
            else:
                print("old mention found (from @{})".format(mention.user.screen_name))

    time.sleep(INTERVAL)
