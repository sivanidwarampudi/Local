#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:11:42 2020

@author: suneelvarma
"""

n = 1000
files = []

for _ in range(n):
    f = open('output1/sample%i.txt'%_,'w')
    files.append(f)
    f.close()