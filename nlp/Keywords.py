#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:45:21 2018

@author: tis
"""

class Keywords:
    
    def __init__(self):
        pass
    
    def aviation(self):
        # 7
        kw_aviation = [
                'boeing',
                'airbus',
                'jet'
                'aircraft',
                'aeroplane',
                'dreamliner',
                'flight'
                ]
        return kw_aviation
    
    def power(self):
        # 7
        kw_power = [
                'electric',
                'solar',
                'nuclear',
                'power',
                'energy',
                'hyrdo',
                'therm'
                ]
        return kw_power
    
    def defence(self):
        # 7
        kw_defence = [
                'missile',
                'fight',
                'bomb',
                'chopper',
                'war',
                'defence',
                'force'
                ]
        return kw_defence
    
    def finance(self):
        # 7
        kw_finance = [
                'financ',
                'bank',
                'loan',
                'invest',
                'stock',
                'equity',
                'debt'
                ]
        return kw_finance
    
    def telecom(self):
        # 7
        kw_telecom = [
                'communication',
                'telecom',
                'phone',
                'mobile',
                'landline',
                'internet',
                'broadband'
                ]
        return kw_telecom
    
    def all_sectors(self):
        return {
                'aviation': self.aviation(),
                'defence': self.defence(),
                'finance': self.finance(),
                'power': self.power(),
                'telecom': self.telecom()
                }
