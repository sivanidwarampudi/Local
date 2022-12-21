# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:24:56 2019

@author: sivan
"""

def processArray(li):
    count=0
    for i in li:
        if i%2==0:
            print(li)
        elif i%2==1:
            count+=1
            if count>=2:
                print(count)
        elif count==1:
            print(li)
li=[]
while True:
        inp=int(input())
        if inp==-1:
            break
        li.append(inp)
processArray(li)


 
            