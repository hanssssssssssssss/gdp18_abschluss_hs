#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:49:47 2018

@author: ich
"""
import urllib.request, json, tweepy
jsonsource = "https://correspsearch.net/quotesalute/abfrage.xql"
jsonsalute = urllib.request.urlopen(jsonsource)
fullsalute = json.loads(jsonsalute.read())
salute = fullsalute['quote']
print(salute)