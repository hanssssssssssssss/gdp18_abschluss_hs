#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:49:47 2018

@author: ich
"""
import urllib.request, json, tweepy

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

jsonsource = "https://correspsearch.net/quotesalute/abfrage.xql"
jsonsalute = urllib.request.urlopen(jsonsource)
fullsalute = json.loads(jsonsalute.read())
salute = fullsalute['quote']
print(salute)

twitterAPI.update_status(status=salute)