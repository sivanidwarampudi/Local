# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:12:28 2019

@author: sivan
"""

s=input("enter string")
n=int(input("enter index"))
e=s[n:]
k=s[n]
c=0
for i in e:
    if k==i:
        c=c+1
print(c-1)
#