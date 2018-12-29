#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:49:47 2018

@author: ich
"""
import urllib.request, json, tweepy

CONSUMER_KEY = 'xqIBv0HqN8iSutUlIVogCaON7'
CONSUMER_SECRET = 'ZxHHXfTlYzplmgEFO8UAKALs4PEovL5Ho1Yh3lswEwdB22dPuh'
ACCESS_KEY = '1078723959632351232-U2QjswT5q9jx49przCiS5ba296POBn'
ACCESS_SECRET = 'hXCl80Kt2VqM8ijxlLxQUj5Xfgh8asG4Ed3o7l1IgSqV9'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitterAPI = tweepy.API(auth)

jsonsource = "https://correspsearch.net/quotesalute/abfrage.xql"
jsonsalute = urllib.request.urlopen(jsonsource)
fullsalute = json.loads(jsonsalute.read())
salute = fullsalute['quote']
print(salute)

twitterAPI.update_status(status=salute)