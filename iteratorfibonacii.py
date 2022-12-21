# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:32:18 2020

@author: sivan
"""

class fibonacii:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a+=self.b
        self.b=self.a
        return self.a
    def __iter__(self):
        return self       
s=fibonacii()