#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Tue Apr 17 23:39:14 2018
@author     : Sourabh
"""

# %%

import sys

# add modules path before importing them
sys.path.insert(0, '../')
    
from pyutils.web import HttpRequest
from pyutils.web import HttpMethod
from pyutils.web import HttpRequestManager
from pyutils.web import HttpProxy
from pyutils.web import HttpProxyCredentials

class TestDriver:
    
    def __init__(self):
        self.reqMgr = HttpRequestManager(logged=True)
        pass
    
    def __proxyDetails(self):
        return HttpProxy(host='', port=0)
    
    def __proxyCredentials(self):
        return HttpProxyCredentials(uname='', passwd='')
    
    def testWebRequest1(self):
        req = HttpRequest(uri='http://date.jsontest.com/')
        self.reqMgr.invoke(req, HttpMethod.GET)
    
    def testWebRequest2(self):
        req = HttpRequest()
        req.uri = 'http://services.groupkt.com/country/search'
        req.queryParams = {'text': 'und'}
        req.headers = {'Accept': 'application/json'}
        self.reqMgr.invoke(req, HttpMethod.GET)
    
    def testWebRequest3(self):
        req = HttpRequest()
        req.uri = 'https://reqres.in/api/users'
        req.headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
                }
        req.payload = {
                "name": "titan",
                "job": "spin and revolve"
                }
        self.reqMgr.invoke(req, HttpMethod.POST)

if __name__ == '__main__':
    td = TestDriver()
    td.testWebRequest1()
    print()
    td.testWebRequest2()
    print()
    td.testWebRequest3()
    print()
    pass
