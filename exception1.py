# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:40:12 2020

@author: sivan
"""

n=int(input())
for i in range(n):
    a,b=input().split()
    if b==0:
        try:
            print(1/0)
        except ZeroDivisionError as e:
            print("Error code:",e)
    elif b!=int(b):
        try:
            print(int(a)/int(b))
        except ValueError as e:
            print("Error code:",e)
    else:
        print(int(a)/int(b))