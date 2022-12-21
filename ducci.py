# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:36:53 2019

@author: sivan
"""
def ducci_sequence(*ns):
    while True:
        yield ns
        ns = list(abs(ns[i - 1] - ns[i]) for i in range(len(ns)))
def ducci(*ns):
    known = list()
    for ns in ducci_sequence(*ns):
        print(ns)
        if ns in known or list(ns) == [0]:
            break
        known.append(ns)
print(ducci(0,653,1854,4063))