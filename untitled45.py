# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:20:12 2019

@author: sivan
"""

def processArray(liste):
    count=0
    for i in liste:
        inde=liste.index(i)
        if i%2==0:                
            if inde!=len(liste)-1:  
                count=count+1    
                x=i            
                liste.remove(x)
                liste.insert(inde,-1)
            if inde==len(liste)-1 and count>1:    
                liste.remove(i)                  
                liste.append(count+1)            
                break
        elif i%2!=0:
            if count==1:        
                liste.remove(-1)
                liste.insert(inde-1,x)
                count=0            
            if count>1 :      
                 liste.insert(inde-1,count)
                 count=0
         
    while -1 in liste:
           liste.remove(-1)

    return len(liste)
liste=[]
while True:
    inp= int(input())
    if inp<0:
        break
    else:
        liste.append(inp)
processArray(liste)
for i in range(len(liste)):
    print(liste[i])