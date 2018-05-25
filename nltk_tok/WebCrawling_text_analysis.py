# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:57:57 2018

@author: kartikaya
"""

import urllib.request

#url = 'https://www.fidelity.co.uk/markets-insights/financial-planning/put-a-foot-on-the-property-ladder'
url2 = 'https://dzone.com/articles/pdf-reading'
from bs4 import BeautifulSoup

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from pyquery import PyQuery   

response = urllib.request.urlopen(url2) 

html = str(response.read())
pq = PyQuery(html)
soup = BeautifulSoup(response.read(),"html.parser")
text = soup.get_text()

text = re.sub('[^a-zA-Z]', ' ' ,text)
text.lower()


tokens = [t for t in text.split()]

freq = nltk.FreqDist(tokens)

for key, val in freq.items():
    print( str(key) +' ' + str(val) )





