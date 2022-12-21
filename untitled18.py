# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:27:12 2019

@author: sivan
"""
l=[x for x in input().split()]
a=[]
t=[]
b=[]
temp=""
ans=[]
for i in l:
    temp=""
    for x in range(1,len(i)-1):
        temp+=i[x]
        t=temp.split(",")
    #print("t:",t)
    for j in set(t):
        a.append(t.count(j))
    #print("a",a)
    b.append(max(a))
    #print("b",b)
    a=[]
    t=[]
#print(b)
ma=max(b)
#print(ma)
for x in b:
    if ma==x:
        ans.append(b.index(x))

if len(set(b))>1:    
    print(ans[0]+1)
else:
    print("0")
