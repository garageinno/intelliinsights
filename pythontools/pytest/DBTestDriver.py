#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Fri Apr 20 00:05:25 2018
@author     : Sourabh
"""

# %%

import sys

sys.path.insert(0, '../../')

from pyutils.db import DatabaseManager
from pyutils.db import Field

# %%

class DBTestDriver:
    
    def __init__(self):
        self.dbm = DatabaseManager()
    
    def testCreateTable(self):
        print('-' * 20, 'DB Read Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        table = 'articles'
        sector = Field('sector', 'varchar(32)')
        file = Field('file_name', 'varchar(256)')
        schema = [sector, file]
        self.dbm.connectDB(dbLoc)
        self.dbm.deleteTable(table)
        self.dbm.createTable(table, schema)
        self.dbm.saveTable(table)
        self.dbm.closeDB()
    
    def testUpdateTable(self):
        print('-' * 20, 'DB Update Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        table = 'articles'
        items = [('Aviation', 'S01_A0001.txt'),
             ('Infrastructure', 'S02_A0010.txt'),
             ('Telecommunication', 'S03_A0100.txt'),
             ('Power', 'S04_A1000.txt'),
             ]
        self.dbm.connectDB(dbLoc)
        self.dbm.insertIntoTable(table, items)
        self.dbm.saveTable(table)
        self.dbm.closeDB()
    
    def testReadTable(self):
        print('-' * 20, 'DB Read Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        table = 'articles'
        self.dbm.connectDB(dbLoc)
        records = self.dbm.fetchAllFromTable(table)
        self.dbm.closeDB()
        print('Result:')
        if records is not None:
            for record in records:
                print(record)
                
    def testReadTableWithQuery(self):
        print('-' * 20, 'DB Read Test', '-' * 20)
        dbLoc = 'testdb.sqlite'
        query = '''
        select * from articles
        where sector is not 'Power'
        order by file_name desc
        '''
        self.dbm.connectDB(dbLoc)
        self.dbm.executeQuery(query)
        records = self.dbm.fetchAll()
        self.dbm.closeDB()
        print('Result:')
        if records is not None:
            for record in records:
                print(record)

if __name__ == '__main__':
    dbtd = DBTestDriver()
    dbtd.testCreateTable()
    print()
    dbtd.testUpdateTable()
    print()
    dbtd.testReadTable()
    print()
    dbtd.testReadTableWithQuery()
    print()
