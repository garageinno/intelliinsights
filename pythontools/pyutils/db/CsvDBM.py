#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 22:57:28 2018
@author     : Sourabh
"""

# %%

from .ConcreteDBM import ConcreteDBM

class CsvDBM(ConcreteDBM):
    def __init__(self):
        super().__init__()
        pass
    
    def connectDB(self, dbpath):
        pass
    
    def closeDB(self):
        pass
