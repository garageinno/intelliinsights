# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:21:47 2018

@author: tajbeerrawat
"""
import requests

class HttpRequestTemplate:
    
          
    def fetch_document_urls(self, url):
        listOfDocumentsUrls = []
        req = requests.get(url)
        resp = req.json()
        articles = resp['articles']
        for x in articles:
            listOfDocumentsUrls.append(x['url'])
        return listOfDocumentsUrls
