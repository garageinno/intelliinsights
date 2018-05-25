# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:01:16 2018

@author: kartikaya
"""

import os
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import operator
from article_data_preprocessor_util import word_count, hit_count
import docx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


real_estate_keywords = ['house', 'propert', 'properti','property','home', 'mortgag', 'mortgage','estate', 'estat']
retail_keywords = ['retail', 'retai', 'shop', 'amazon' , 'sale', 'supermarket' , 'groceri']
energy_keywords = ['oil','commod', 'gas', 'shale', 'shal', 'solar', 'e-car', 'e-vehicle', 'middle east', 'opec', 'shell', 'bp', 'chevron', 'barrel','energy', 'energi']

xcel = pd.read_excel('C:\\Users\\kartikaya\\Python_Data\\Article_Search_MindTrust\\FUNDS\\Funds-sectors.xlsx')
funds = xcel.iloc[:, 0]
tags = xcel.iloc[:, 1]
isin = xcel.iloc[:, 2]
all_files = os.listdir("C:\\Users\\kartikaya\\Python_Data\\Article_Search_MindTrust\\Articles") 


corpus = []

ps = PorterStemmer()
j = 0
for article in all_files:
        file = 'C:\\Users\\kartikaya\\Python_Data\\Article_Search_MindTrust\\Articles\\' + all_files[j]
        j = j + 1
        doc = docx.Document(file)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
            '\n'.join(full_text)
        article_cleaned = ''
        for text in full_text:
            text = re.sub('[^a-zA-Z]',' ',text)
            article_cleaned = article_cleaned + text
        article_cleaned = article_cleaned.lower()
        article_cleaned = article_cleaned.split()
        article_cleaned = [ps.stem(word) for word in article_cleaned if not word in set(stopwords.words('english'))]
        article_cleaned = ' '.join(article_cleaned)
        corpus.append(article_cleaned)
        

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X_vector = cv.fit_transform(corpus).toarray()

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X_vector)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X_vector)
y_kmeans.sort()

# Visualising the clusters
plt.scatter(X_vector[y_kmeans == 0, 0], X_vector[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X_vector[y_kmeans == 1, 0], X_vector[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X_vector[y_kmeans == 2, 0], X_vector[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.legend()
plt.show()