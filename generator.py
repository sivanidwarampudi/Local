# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:46:14 2020

@author: sivan
"""
"""l=[1,23,4]
nl=[x**2 for x in l]"""
"""def eve():
    a=0
    b=1
    while True:
        yield a//yield a,b is also possible
        a,b=b,a+b
f=eve()"""
def fun():
    a=0
    while True:
        x=yield a 
        if x is not None:
            a=x+2
        else:
            a=a+2
            """by default yields returns none when we send something it wont return none
            first yield something then send something"""
            
f=fun()