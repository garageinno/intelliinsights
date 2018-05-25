#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:50:03 2018

@author: tis
"""

import os
import re
#import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#from nltk.probability import FreqDist
import operator
import pandas as pd

#import sys
#sys.path.insert(0, '../pythontools')

#from pyutils.io import FileManager


real_estate_keywords = ['house', 'propert', 'properti','property','home', 'mortgag', 'mortgage','estate', 'estat']
retail_keywords = ['retail', 'retai', 'shop', 'amazon' , 'sale', 'supermarket' , 'groceri']
energy_keywords = ['oil','commod', 'gas', 'shale', 'shal', 'solar', 'e-car', 'e-vehicle', 'middle east', 'opec', 'shell', 'bp', 'chevron', 'barrel','energy', 'energi']

#xcel = pd.read_excel('C:\\Users\\kartikaya\\Python_Data\\Article_Search_MindTrust\\FUNDS\\Funds-sectors.xlsx')
#funds = xcel.iloc[:, 0]
#tags = xcel.iloc[:, 1]
#isin = xcel.iloc[:, 2]

all_articles_aviation = os.listdir("./articles/aviation")
all_articles_defence = os.listdir("./articles/defence")
all_articles_finance = os.listdir("./articles/finance")
all_articles_power = os.listdir("./articles/power")
all_articles_telecom = os.listdir("./articles/telecom")

fm = FileManager()

ps = PorterStemmer()
j = 0

# %%
article_list = []
#for article in all_articles_aviation:
article = 'data2.txt'
file = './articles/defence/' + article
full_text = fm.read(file)
article_cleaned = re.sub('[^a-zA-Z]',' ', full_text)
article_cleaned = article_cleaned.lower()
article_cleaned = article_cleaned.split()

article_cleaned = [ps.stem(word) for word in article_cleaned if not word in set(stopwords.words('english'))]

#import nltk
#nltk.download('stopwords')

article_cleaned = ' '.join(article_cleaned)
count = count_frequency(article_cleaned)

sorted_x = sorted(count.items(), key=operator.itemgetter(1), reverse = True)

# %%


df = pd.read_csv('kwd_list.txt')
kwd_list = df.iloc[:,0]
word_hits = hit_count(sorted_x, kwd_list)


retail_hits  = hit_count(sorted_x , retail_keywords)
energy_hits = hit_count(sorted_x, energy_keywords)
if fund_tags == 'energy' and energy_hits > 10:
    article_list.append(article)
if fund_tags == 'real_estate' and real_estate_hits > 10:
    article_list.append(article)
i=1
print('Relevant Articles : ')
for article in article_list:
    print(str(i) + '-> '+ article)
    i = i + 1


#
#while 1 == 1:
#    i = 1
#    print('------------------------------------------------------------')
#    print('------------------------------------------------------------')
#    print('Please select a fund')
#    for fund in funds:
#        print(str(i)+" - "+str(fund))
#        i = i + 1
#    print('------------------------------------------------------------')
#    print('------------------------------------------------------------')
#    fund = input(" ")
#    fund = fund.strip()
#    index = int(fund) - 1
#    string = funds[index]
#    print('you selected : '+string)
#    fund_tags = tags[index]
#    fund_isin = isin[index]
#
#    


def count_frequency(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
    
    
    
def hit_count(sorted_tuple_list, keywords):
    hits = 0
    for tuple in sorted_tuple_list:
     for word in keywords:
        if(word == tuple[0]):
          hits = hits + tuple[1]
    return hits
