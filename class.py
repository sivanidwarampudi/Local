# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:25:10 2020

@author: sivan
"""
class stt:
    def __init__(self):
        self.a=0
    def __next__(self):
        self.b=self.a
        self.a+=2
        return self.b
    def __iter__(self):
        return self
s=stt()