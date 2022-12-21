# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:41:10 2019

@author: sivan
"""
def findEleven(listOfNumbers):
    for i in listOfNumbers:
        if (i==11):
            return True
        else:
            return False
if __name__ == '__main__':
    size = int(input())
    for i in range(size+1):
     listOfNumbers = [int(x) for x in input().split()]
    print(findEleven(listOfNumbers))