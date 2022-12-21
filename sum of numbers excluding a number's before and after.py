# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 11:44:23 2019

@author: sivan
"""

def sumofnum(li,ex):
    sum=0
    for i in range(0,len(li)):
        sum=sum+li[i]
        if i==ex:
            sum=sum-(li[i-1]-li[i+1])
    return sum
if __name__== "__main__":
    n=int(input())
    li=[]
    for i in range(0,n):
        li.append(int(input()))
    ex=int(input())
    print(sumofnum(li,ex))
    