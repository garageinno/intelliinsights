#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 22:58:00 2018
@author     : Sourabh
"""

# %%

from .ConcreteDBM import ConcreteDBM

class MysqlDBM(ConcreteDBM):
    def __init__(self):
        super().__init__()
        pass
    
    def connectDB(self, dbpath):
        pass
    
    def closeDB(self):
        pass
