# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:39:46 2019

@author: sivan
"""

"""f = open("text.txt", "rb")
s = f.readlines()
f.close()
f = open("newtext.txt", "wb")
s.reverse()
for item in s:
  print>>f, item
f.close()"""

"""f2=open('test.txt','w')
for i in l:
    for j in i.split():
        f.write(j[::-1])
        f.write(' ')
    f.write('\n')"""
    
data = data2 = "" 
with open('file1.txt') as fp: 
	data = fp.read() 
with open('file2.txt') as fp: 
	data2 = fp.read()  
data += "\n"
data += data2 
with open ('file3.txt', 'w') as fp: 
	fp.write(data) 
