# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:25:44 2018

@author: tajbeerrawat
"""



import requests
import sys
from bs4 import BeautifulSoup
import csv

def fetch_document_urls(url):
    listOfDocumentsUrls = []
    req = requests.get(url)
    resp = req.json()
    articles = resp['articles']
    for x in articles:
        listOfDocumentsUrls.append(x['url'])
    return listOfDocumentsUrls;

def print_urls(listOfDocumentsUrls):
    for y in range(0,len(listOfDocumentsUrls)-18):
        print(listOfDocumentsUrls[y])
        
def main(url):
    documentUrls = fetch_document_urls(url)
    for i in range(0, len(documentUrls)):
        data = scrap_data_from_url(documentUrls[i])
        save_to_csv(data, "data"+str(i)+".csv")
    

def scrap_data_from_url(url):
    response = requests.get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    article_text = ''
    for content in html_soup.select("[class^='content-well'] p"):
        article_text += ''.join(content.text)
    return article_text
    
def save_to_csv(data, file_name):
    with open(file_name, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([data])


    
        
if(__name__ == '__main__'):
   main(sys.argv[1])
    

    
    
    
    
    