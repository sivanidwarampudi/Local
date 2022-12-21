# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 08:55:57 2020

@author: sivan
"""

class point:
    def __init__(self,a,b):
        self.x=a
        self.y=b
class polygon:
    def __init__(self):
        self.points=[]
    def addpoint(self,o):
        self.obj=o
class polygon:
    def __init__(self):
        self.points=[]
    def addpoint(self,o):
        self.points.append(o)
    def showpoints(self):
        for p in self.points:
            print((p.x,p.y))
""" p=point(1,2)

rect=polygon

rect=polygon()

rect.addpoint(p)

rect.addpoint(point(2,3))

rect.addpoint(point(4,5))

rect.addpoint(point(6,7))

rect.showpoints
Out[16]: <bound method polygon.showpoints of <__main__.polygon object at 0x000001BF44510FC8>>

rect.showpoints()
(1, 2)
(2, 3)
(4, 5)
(6, 7)
"""
class details:
    l=[]
    def __init__(self,name,pno):
        self.name=name
        self.pno=pno
        details.l.append(self)
    def show_details(self):
        return details.l

