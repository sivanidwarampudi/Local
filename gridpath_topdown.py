# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:53:07 2019

@author: sivan
"""


d={}
d[(0,0)]=1

def tdpath(i,j):
    if d.get((i,0),-1)!=-1:
        return 1
    elif d.get((0,j),-1)!=-1:
        return 1
    else:
        return tdpath(i-1,j)+tdpath(i,j-1)
        
if __name__=="__main__":
    i=int(input())
    j=int(input())
    import timeit
    start=timeit.default_timer()
    print(tdpath(i,j))
    end=timeit.default_timer()
    print("Time taken in seconds is",end-start)    

        
    
    
    


