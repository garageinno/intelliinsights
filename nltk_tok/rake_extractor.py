# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:16:32 2018

@author: kartikaya
"""

import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.probability import FreqDist
import operator

import docx
import pandas as pd
from rake_nltk import Rake


xcel = pd.read_excel('C:\\Users\\kartikaya\\Python_Data\\Article_Search_MindTrust\\FUNDS\\Funds-sectors.xlsx')
funds = xcel.iloc[:, 0]
tags = xcel.iloc[:, 1]
isin = xcel.iloc[:, 2]
all_files = os.listdir("C:\\Users\\kartikaya\\Python_Data\\Article_Search_MindTrust\\Articles")

file = 'C:\\Users\\kartikaya\\Python_Data\\Article_Search_MindTrust\\Articles\\' + all_files[0]

doc = docx.Document(file)

full_text = []

for para in doc.paragraphs:
    full_text.append(para.text)
    '\n'.join(full_text)

    
r = Rake()
r.extract_keywords_from_text(str(full_text))
print(r.get_ranked_phrases_with_scores())

