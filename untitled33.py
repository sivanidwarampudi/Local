# -*- coding: utf-8 -*-
#exec(print('stt'))
#print(eval('4+5'))
#print(repr('sivani'))
n=[x for x in input().split()]
n1=int(input("Index of an element to delete"))
n2=int(input("Index of an element to insert"))
l=[]
l1=[]
l2=[]
l=l1
l=l2
for i in range(len(n)):
    l.append(n)
    l1.remove(n1)
    l2.insert(n2)
print(l)
print(l1)
print(l2)