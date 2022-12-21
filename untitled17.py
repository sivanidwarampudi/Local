# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:31:31 2019

@author: sivan
"""

#to read character by character
"""c=f.read(1)
while c:
    print(c)
    c=f.read(1)"""
    
   #open(r"C:\Users\sivan\OneDrive\Desktop\abc.txt") 
   """
   Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
Type "copyright", "credits" or "license" for more information.

IPython 7.8.0 -- An enhanced Interactive Python.

f=open("abc.txt","r")
Traceback (most recent call last):

  File "<ipython-input-1-8af468918195>", line 1, in <module>
    f=open("abc.txt","r")

FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'




f=open("\rabc.txt","r")
Traceback (most recent call last):

  File "<ipython-input-2-6e785c5c0a98>", line 1, in <module>
    f=open("\rabc.txt","r")

OSError: [Errno 22] Invalid argument: '\rabc.txt'




f=open(\r"abc.txt","r")
  File "<ipython-input-3-09636f523bfc>", line 1
    f=open(\r"abc.txt","r")
                           ^
SyntaxError: unexpected character after line continuation character




f=open(\r"C:\Users\sivan\OneDrive\Desktop","r")
  File "<ipython-input-4-c2086392438e>", line 1
    f=open(\r"C:\Users\sivan\OneDrive\Desktop","r")
                                                   ^
SyntaxError: unexpected character after line continuation character




f=open(\r"C:\Users\sivan\OneDrive\Desktop")
  File "<ipython-input-5-5643c884d04d>", line 1
    f=open(\r"C:\Users\sivan\OneDrive\Desktop")
                                               ^
SyntaxError: unexpected character after line continuation character




f=open(\r"C:\Users\sivan\OneDrive\Desktop\abc.txt")
  File "<ipython-input-6-abef3e52b1f3>", line 1
    f=open(\r"C:\Users\sivan\OneDrive\Desktop\abc.txt")
                                                       ^
SyntaxError: unexpected character after line continuation character




f=open("\r \C:\Users\sivan\OneDrive\Desktop\abc.txt")
  File "<ipython-input-7-85f8866cf205>", line 1
    f=open("\r \C:\Users\sivan\OneDrive\Desktop\abc.txt")
          ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 6-7: truncated \UXXXXXXXX escape




f=open(\r"\C:\Users\sivan\OneDrive\Desktop\abc.txt")
  File "<ipython-input-8-658977f5770b>", line 1
    f=open(\r"\C:\Users\sivan\OneDrive\Desktop\abc.txt")
                                                        ^
SyntaxError: unexpected character after line continuation character




f=open(r"\C:\Users\sivan\OneDrive\Desktop\abc.txt")
Traceback (most recent call last):

  File "<ipython-input-9-912f485c629f>", line 1, in <module>
    f=open(r"\C:\Users\sivan\OneDrive\Desktop\abc.txt")

OSError: [Errno 22] Invalid argument: '\\C:\\Users\\sivan\\OneDrive\\Desktop\\abc.txt'




f=open(r"C:\Users\sivan\OneDrive\Desktop\abc.txt")

f1="this is write"

f1.write(45)
Traceback (most recent call last):

  File "<ipython-input-12-761845473d33>", line 1, in <module>
    f1.write(45)

AttributeError: 'str' object has no attribute 'write'




s=
  File "<ipython-input-13-1974461997b0>", line 1
    s=
      ^
SyntaxError: invalid syntax




s="fcvevcefvc"

f.write(s)
Traceback (most recent call last):

  File "<ipython-input-15-6b1dd4b3d221>", line 1, in <module>
    f.write(s)

UnsupportedOperation: not writable




f=open(r"C:\Users\sivan\OneDrive\Desktop\abc.txt","w")

s="fcvevcefvc"

f.write(s)
Out[18]: 10

f.flush()

f
Out[20]: <_io.TextIOWrapper name='C:\\Users\\sivan\\OneDrive\\Desktop\\abc.txt' mode='w' encoding='cp1252'>

s="fcvevcefvc"

f.write(s)
Out[22]: 10

f.tell()
Out[23]: 20

f.truncate(3)
Out[24]: 3

f.truncate(8)
Out[25]: 8

f
Out[26]: <_io.TextIOWrapper name='C:\\Users\\sivan\\OneDrive\\Desktop\\abc.txt' mode='w' encoding='cp1252'>

s=f.read()
Traceback (most recent call last):

  File "<ipython-input-27-2bcd0fcfb433>", line 1, in <module>
    s=f.read()

UnsupportedOperation: not readable




f=open(r"C:\Users\sivan\OneDrive\Desktop\abc.txt","w")

s=f.read()
Traceback (most recent call last):

  File "<ipython-input-29-2bcd0fcfb433>", line 1, in <module>
    s=f.read()

UnsupportedOperation: not readable




l=f.readlines()
Traceback (most recent call last):

  File "<ipython-input-30-326e20cdb4c4>", line 1, in <module>
    l=f.readlines()

UnsupportedOperation: not readable




f=open(r"C:\Users\sivan\OneDrive\Desktop\abc.txt","r")

l=f.readlines()

l
Out[33]: []

s="dsccdxdcsc"

f.write(s)
Traceback (most recent call last):

  File "<ipython-input-35-6b1dd4b3d221>", line 1, in <module>
    f.write(s)

UnsupportedOperation: not writable




print
Out[36]: <function print>

(print)
Out[37]: <function print>

dir("print")
Out[38]: 
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isascii',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']

f1=('t.txt','w')

for line in l:
    print(line,file=f2)
    

for line in l:
    print(line,file=f1)
    

f1.flush()
Traceback (most recent call last):

  File "<ipython-input-42-ba488a72735e>", line 1, in <module>
    f1.flush()

AttributeError: 'tuple' object has no attribute 'flush'




f=('abc.txt','w')

f="rfrrfrverfv
  File "<ipython-input-44-eb2132277394>", line 1
    f="rfrrfrverfv
                  ^
SyntaxError: EOL while scanning string literal"""
