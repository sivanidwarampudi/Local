#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:41:18 2020

@author: suneelvarma
"""


'''PRACTICE'''

import threading
import requests
import queue

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        print('downloading...')
        downloader()
        print('downloaded')
        
        
    
def downloader():
    
    while True:
        try:   
            link,img_id = image_links.get(block=False)
        except:
            return
        else:
            create_filensave(link,img_id)
            
            
def create_filensave(link,img_id):
    global category
    image = requests.get(link)
    filename = category+str(img_id)+'.jpg'
    
    with open(filename,'wb') as fileobj:
        fileobj.write(image.content)
        fileobj.close()
    return


#image_links in a queue
    
category= str(input("What kind of images you need? \nExample Keywords:\nbooks\nbicycle\nbike\nbeach.\n\nEnter any keyword: "))    
links= ["https://source.unsplash.com/1600x900/?"+category]*12

image_links = queue.Queue()
for img_id,link in enumerate(links):
    image_links.put((link,img_id))
    
#threads
threads = [MyThread() for _ in range(12)]
for thread in threads: thread.start()
for thread in threads: thread.join()
print('DONE')