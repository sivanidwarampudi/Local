# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:45:31 2019

@author: sivan
"""

"""given rods of 1m 2m 3m length and their costs in list
 given a rod of length l when will you get max profit
"""
"""d={}
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
    print("Time taken in seconds is",end-start)""" 

p=[1,5,8,9,10,17,17,20,24,30]
def mp(n,l):
    if n==0:
        return 0
    q=-999999999999999999999999999
    for i in range(1,len(n)+1):
        if n>=i:
            q=max(q,n[i-1]+mp(n,l-i))
    return q
#print(mp(l,10))      
#topdowm
d={}
def mp(n,l):
    if n in d:
        return d[n]
    else:
        if n==0:
            return 0
        else:
            t=0
            for x in range(len(l)):
                if x+1<=n:
                    t=max(t,l[x]+mp(n-(x+1),l))
            d[n]=t
            return t
#print(mp(3,l))
    
       
"""if __name__=="__main__":
    p=int(input())
    n=int(input())
    import timeit
    start=timeit.default_timer()
    print(mp(p,n))
    end=timeit.default_timer()
    print("Time taken in seconds is",end-start) """
