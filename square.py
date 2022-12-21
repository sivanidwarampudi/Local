# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:21:40 2020

@author: sivan
"""
def square(n):
    i=1
    while i*i<=n:
        j=1
        while i*i<=n:
            if i*i+j*j==n:
                return True
            j+=1
        i+=1
    return False
if __name__=='__main__':
    n=int(input())
    print(square(n))