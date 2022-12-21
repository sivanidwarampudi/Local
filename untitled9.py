# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:29:11 2019

@author: sivan
"""
n=int(input())
arr=[i for i in input().split()]
l=[]
x=max(arr)
l=arr.remove(x)
for i in range(n):
    l.append(arr)
    print(max(l))