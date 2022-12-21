# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:29:07 2019

@author: sivan
"""

n = int(input())
arr = list(map(int, input().split()))
listnew=[]
for i in arr:
    if i not in listnew:
        listnew.append(i)
        listnew.sort(reverse=True)
print(listnew[1])