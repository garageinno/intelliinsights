# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 13:14:19 2018

@author: tajbeerrawat
"""
import requests

from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.bloomberg.com/news/articles/2018-02-21/netanyahu-legal-woes-worsen-as-ex-top-aide-agrees-to-testify")
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
article_text = ''
for content in html_soup.select("[class^='content-well'] p"):
    #print(content.text)
    article_text += ''.join(content.text)
    print(article_text)
    
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
	 #writer.writerow([name, price, datetime.now()])
    writer.writerow([article_text])