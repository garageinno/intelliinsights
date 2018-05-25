#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 00:41:21 2018
@author     : Sourabh
"""

# %%

import sys

# add modules path before importing them
sys.path.insert(0, '../../')

from pyutils.io import FileManager

class FileTestDriver:
    
    def __init__(self):
        self.fm = FileManager()
        pass
    
    def testFileRead(self):
        print('-' * 20, 'Read Test', '-' * 20)
        fileLoc = 'Sample.txt'
        contents = self.fm.read(fileLoc)
        if contents is not None:
            print(contents)
        pass
    
    def testFileWrite(self):
        print('-' * 20, 'Write Test', '-' * 20)
        fileLoc = 'Sample.txt'
        contents = 'This is purely a dummy text.\nModi lies...\n'
        self.fm.write(fileLoc, contents)
        pass
    
if __name__ == '__main__':
    ftd = FileTestDriver()
    ftd.testFileRead()
    print()
    ftd.testFileWrite()
    print()
    pass
