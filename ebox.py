# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:42:14 2020

@author: sivan
"""

def number(n):
    while n>0:
        n=list(n)
        n[1]=n[0]+2
        n[2]=n[1]+2
        
    
if __name__=='__main__':
    n=int(input())
print(number(n))