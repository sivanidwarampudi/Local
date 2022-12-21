# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:31:30 2020

@author: sivan
"""

"""f=open('data.txt','r')
s=f.read()
print(s)
f.close()
x=input("enter username")
f=open("data.txt",'w')
f.write(x)
print(f)
f.close()"""
""""f=input().split()
print(f)"""
n=int(input())
stud={}
for _ in range(n):
    line=input().split()
    names,score=line[0],line[1:]
    score=map(float,score)
    stud[name]=score