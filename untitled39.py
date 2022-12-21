# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 14:57:37 2019

@author: sivan
"""

def processArray(love):
    cis=0
    for i in range(len(love)):
        if(love[i]<=10):
            cis=cis+1
    return cis
liste=[]
while True:
        smile=int(input())
        if smile==-1:
            break
        liste.append(smile)
print(processArray(liste))