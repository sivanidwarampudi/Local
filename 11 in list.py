# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:12:37 2019

@author: sivan
"""

def findEleven(listOfNumbers):
    for i in range(0,5):
        print(len(listOfNumbers))
        if i<len(listOfNumbers):
            if listOfNumbers[i]==11:
                return True
    return False
    #Fill your code
        

if __name__ == '__main__':
    size = int(input())
    listOfNumbers = []
    for i in range(0,size):
        listOfNumbers.append(int(input()))
    print(findEleven(listOfNumbers))