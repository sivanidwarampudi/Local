# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:35:00 2019

@author: sivan
"""

try:
    print("before")
    1/0
    print("after")
except ZeroDivisionError:
    print("caught")
