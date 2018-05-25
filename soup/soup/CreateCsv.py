# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:50:15 2018

@author: tajbeerrawat
"""
import csv
import pathlib
class CreateCsv:
    """ Create CSV for WebScrapped data on a user passed location"""
    location = None
    
    def __init__(self, location):
        if location is not None:
            self.location = './articles/' + location
        else:
            self.location = './articles/'
        
        pathlib.Path(self.location).mkdir(parents=True, exist_ok=True) 
            
    
    def create_csv(self, data, file_name):
        with open(self.location+'/'+file_name, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([data])