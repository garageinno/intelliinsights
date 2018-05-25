# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:25:44 2018

@author: tajbeerrawat
"""



import requests
def invokeRequest(url):
    listOfDocumentsUrls = []
    req = requests.get("https://newsapi.org/v2/everything?q=Telecommunication&sources=bloomberg&apiKey=2b4c0aaa81c141f9a35a29bf098bc0b6")
    resp = req.json()
    articles = resp['articles']
    
    for x in articles:
        listOfDocumentsUrls.append(x['url'])

    for y in listOfDocumentsUrls:
        print(y)
    
    
    
    
    