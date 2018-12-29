#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:49:47 2018

@author: ich
"""
import urllib.request, json, tweepy

#Example values
CONSUMER_KEY = 'EXAMPLEKEY'
CONSUMER_SECRET = 'EXAMPLE'
ACCESS_KEY = 'EXAMPLEKEY'
ACCESS_SECRET = 'EXAMPLE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitterAPI = tweepy.API(auth)

jsonsource = "https://correspsearch.net/quotesalute/abfrage.xql"
jsonsalute = urllib.request.urlopen(jsonsource)
fullsalute = json.loads(jsonsalute.read())
salute = fullsalute['quote']
print(salute)

twitterAPI.update_status(status=salute)