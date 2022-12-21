# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:33:45 2019

@author: sivan
"""

l=[]
k=[]
a=int(input())
while(a!=-1):
    l.append(a)
    a=int(input()) 
for i in range(len(l)):
    if l[i]%2==0:
        k.append(l[i])
        c=0
    else:
        c=c+1
        if c>=2 and l[i+1]%2==0:
            k.append(c)
            c=0
        elif c>=2 and l[i+1]%2!=0:
            continue
        elif c==1 and i<len(l)-1:
            if l[i+1]%2==0:
                k.append(l[i])
        elif c==1 and i==len(l)-1:
            k.append(l[i])
for i in k:
    print(i)