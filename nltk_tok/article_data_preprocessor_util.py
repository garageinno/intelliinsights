# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:53:04 2018

@author: kartikaya
"""

def word_count(str):
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