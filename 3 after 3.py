# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 11:36:18 2019

@author: sivan
"""

def findSequence(listOfNumbers):
    # Fill your code
    for i in range(0,size+1):
        if (listOfNumbers[i]==3 and listOfNumbers[i+1]==3):
            c=1
    if c==1:
        return True
    else:
        return False
if __name__ == '__main__':
    size = int(input())
    listOfNumbers = []
    for i in range(0,size):
        listOfNumbers.append(int(input()))
    print(findSequence(listOfNumbers))