# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:00:11 2019

@author: sivan
"""
l=[int(x) for x in input().split()]
l1=[]
for i in range(len(l)):
    l[i]=l[i+1]-l[i]
    l[i+1]=l[i+2]-l[i+1]
    l[i+2]=l[i+3]-l[i+2]
    l[i+3]=l[i+3]-l[i]
    l1.append(l[i])
    l1.append(l[i+1])
    l1.append(l[i+2])
    l1.append(l[i+3])
    print(l1)
