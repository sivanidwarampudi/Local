#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:17:48 2020

@author: suneelvarma
"""


# ch3/my_thread.py

import threading
import time

class SexyThread(threading.Thread):
    
    def __init__(self,name,delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        
    def run(self):
        print('Thread %s started..'%(self.name))
        thread_function(self.name,self.delay)
        print('Thread %s ended..'%(self.name))
        

def thread_function(name,delay):
    
    counter = 5
    
    while counter:
        time.sleep(delay)
        counter -= 1
        print('%s thread count %i'%(name,counter))
        
    return







