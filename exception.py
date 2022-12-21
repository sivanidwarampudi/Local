# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:45:32 2020

@author: sivan
"""

maps={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9',}
def convert(s):
    n=' '
    for token in s:
        n+=maps[token]
    x=int(n)
    return x
    