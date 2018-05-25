# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:17:44 2018

@author: tajbeerrawat
"""
from bs4 import BeautifulSoup
import requests

class WebScrapDataUtil:
    
        
    def scrap_data_from_url(self, url):
        response = requests.get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        type(html_soup)
        article_text = ''
        for content in html_soup.select("[class^='content-well'] p"):
            article_text += ''.join(content.text)
        return article_text
        