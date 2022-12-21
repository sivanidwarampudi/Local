# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:29:27 2019

@author: sivan
"""

l=[1,3.3,45,5.6,3]
l1=[]
l2=[]
for i in range(len(l)):
    if type(l[i]) is int:
        l1.append(l[i])
    elif type(l[i]) is float:
        l2.append(l[i])
print(l1)
print(l2)
    