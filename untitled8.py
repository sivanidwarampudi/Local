# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:08:31 2019

@author: sivan
"""

n = int(input())
arr = list(map(int, input().split()))
zes = max(arr)
i=0
while(i<n):
    if zes ==max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))