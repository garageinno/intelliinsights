#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 23:12:56 2018
@author     : Sourabh
"""

# %%

from .AbstractDBM import AbstractDBM

class ConcreteDBM(AbstractDBM):
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connectDB(self, dbpath):
        pass
    
    def closeDB(self):
        pass
    
    def createTable(self, schema):
        pass
    
    def deleteTable(self, name):
        pass
    
    def saveTable(self, name):
        pass
    
    def executeQuery(self, query):
        pass
    
    def fetchOne(self):
        return self.cursor.fetchone()
    
    def fetchAll(self):
        return self.cursor.fetchall()
