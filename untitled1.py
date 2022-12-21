# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:44:00 2019

@author: sivan
"""
s="ddcuyfvyfvjyvf ygygyyffff gygygiuggvtt tgtbrtbrt bhgtrbhrtgrtgrg tbrtbrtbr\n fvfvfvvv f b\n mfkvkmv"
d={}
for lno,line in enumerate(s.splitlines(),start=1):
    for word in line.split():
        d.setdefault(word,[]).append(lno)