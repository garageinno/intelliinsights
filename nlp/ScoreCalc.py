#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:15:30 2018

@author: tis
"""

import sys

# add modules path before importing them
sys.path.insert(0, '../pythontools')

from pyutils.io import FileManager
from Keywords import Keywords

class ContentReader:

    def __init__(self):
        self.fm = FileManager()
        self.kw = Keywords()
        self.rel_path = './articles/'
    
    def read_file(self, fileLoc):
        contents = self.fm.read(fileLoc)
        return contents
    
    def article_for_sector(self, sector):
        last_index = 10
        scores = {}
        for i in range(0, last_index):
            path = self.rel_path + '/' + sector + '/data' + str(i) + '.txt'
            content = self.read_file(path)
            scores[path] = self.calculate_score(content)
        return scores
    
#    def calculate_score1(self, article):
#        kw_dict = self.kw.all_sectors()
#        for key, values in kw_dict.items():
#            print('Trying for sector: ', key)
#            count = 0
#            kw_count = {}
#            for keyword in values:
#                if keyword in article:
#                    count = count + 1
#            kw_count[key] = count
    
    def calculate_score(self, article):
        kw_dict = self.kw.all_sectors()
        kw_count = {}
        for sector, keywords in kw_dict.items():
#            print('Trying for sector:', sector)
            count = 0
            for keyword in keywords:
                if keyword in article:
                    count = count + 1
            kw_count[sector] = count
        return kw_count

if __name__ == '__main__':
    cr = ContentReader()
    print(cr.article_for_sector('power'))
