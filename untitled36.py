# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:03:08 2019

@author: sivan
"""
l=[int(x) for x in input().split(" ")]
deli=int(input())
insi=int(input())
val=l[deli]
print("Original list {}".format(l))
l.remove(val)
print("List After removing element at index {} {}".format(deli,l))
l.insert(insi,val)
print("List after Adding element at index {} {}".format(insi,l))
l.append(val)
print("List after Adding element at last {}".format(l)