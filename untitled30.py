# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:58:07 2019

@author: sivan
"""

import sys
li=[]
for p in sys.argv[1:]:
    li+=eval(p)
li.sort()
print(li)
    