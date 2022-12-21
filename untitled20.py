# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:24:41 2019

@author: sivan
"""
l=eval(input())
k=max(l)
t=[]
r=l.index(k)
t.append(r)
for i in range(r+1,len(l)):
    if l[i]==k:
        t.append(i)
lt=len(t)        
if lt==1:
    t.append(r)
lt1=[]
if lt>2:
    lt1.append(t[0])
    lt1.append(t[lt-1])
if len(t)==2:
    print(tuple(t))
else:
    print(tuple(lt1))
