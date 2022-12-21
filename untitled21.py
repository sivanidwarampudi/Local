# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:27:08 2019

@author: sivan
"""
def number0f2s(n): 
	count = 0
	while (n > 0): 
	
		if (n % 10 == 2): 
			count = count + 1

		n = n // 10
	
	return count 
def numberOf2sinRange(n): 

	count = 0
	for i in range(2, n + 1): 
		count = count + number0f2s(i) 

	return count 
n=int(input())
print(numberOf2sinRange(n)) 



 