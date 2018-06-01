# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:25:44 2018

@author: tajbeerrawat
"""



from HttpRequestTemplate import HttpRequestTemplate
from WebScrapDataUtil import WebScrapDataUtil
from CreateCsv import CreateCsv
#import sys


def fetch_document_urls(url):
   x = HttpRequestTemplate()
   return x.fetch_document_urls(url)

       
def main(url, doc_limit, directory):
    documentUrls = fetch_document_urls(url)
    scrapper = WebScrapDataUtil()
    to_csv = CreateCsv(directory)
    doc_limit = int(doc_limit)
    if doc_limit > len(documentUrls):
        print('Result is less than document limit')
    else :
        for i in range(0, doc_limit): 
            data = scrapper.scrap_data_from_url(documentUrls[i])
            to_csv.create_csv(data, "data"+str(i)+".txt")
    

   
if __name__ == '__main__':
#   print('%s\n%s\n%s', sys.argv[1], sys.argv[2], sys.argv[3])
#   main(sys.argv[1], sys.argv[2], sys.argv[3])
#    url1 = 'https://newsapi.org/v2/everything?q=banking&sources=bloomberg&apiKey=8d9d17e88d5f48d98a68ca37693eeed8'
    url1 = 'https://newsapi.org/v2/everything?q=infrastructure&sources=bloomberg&apiKey=8d9d17e88d5f48d98a68ca37693eeed8'
    doc_limit = 20
    dir1 = 'infrastructure'
    
    main(url1, doc_limit, dir1)
