# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:35:43 2020

@author: sivan
"""

"""s = 'abcdefghi'
it = iter(s)
for part in zip(it, it, it):
    print(part)
    print(next(it))"""

"""string=input()
k=int(input())
for i in range(0, len(string), k):
    s = ""
    for j in string[i : i + k]:
        if j not in s:
            s += j 
    print(s)"""
    
"""S, N = input(), int(input()) 
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c,c) for c in part if c not in d]))"""
import string
alpha = string.ascii_lowercase

def print_rangoli(n):
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
    print(L[:0:-1])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)