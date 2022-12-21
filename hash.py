# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 02:49:25 2020

@author: sivan
"""

import math as m
f=open('output.txt','w')

bld=[int(x) for x in input().split()] #books,library,days
up_books=list()
scores=[int(x) for x in input().split()]  #scores of books

func=[] #no of books, sign up,limit
func_book=[]    #id's of books which are to be compared with scores
l1=[]
for i in range(bld[1]):
    l=[int(x) for x in input().split()]
    l1.append(l[1])   #now l1 will have sigup number
    func.append(l)
    func_book.append([int(x) for x in input().split()])

lib=0
whichfir=[]
libsend=[]
no_days=bld[2]
#for i in range(bld[2]):
f.write(str(2)+'\n')
for i in range(bld[1]):
    if no_days<=0:
        break
    lib+=1
    dup=""
   
    ind=l1.index(min(l1))    
   
    dup=str(ind)+' '
    no_days=bld[2]-func[ind][1]
    func_book.sort()
    if m.ceil(func[ind][1]/func[ind][2])<no_days:
        up_books.extend([func_book[ind]])
        dup+=str(len(func_book[ind]))+'\n'
#        "".join([str(x) for x in func_book[ind]])
#        dup.append(len(func_book[ind]))
#        libsend.append(func_book[ind])
        aa=func_book[ind]
#        f.write(" ".join([str(x) for x in func_book[ind]])+'\n')
    else:
        up_books.extend([func_book[:no_days*func[ind][2]]])
#        dup.append(len(func_book[:no_days*func[ind][2]]))
        dup+=str(len(func_book[:no_days*func[ind][2]]))
#        "".join([str(x) for x in func_book[:no_days*func[ind][2]]])
        aa=func_book[:no_days*func[ind][2]]
#        f.write(" ".join([str(x) for x in func_book[:no_days*func[ind][2]]])+'\n')

#        libsend.append(func_book[:no_days*func[ind][2]])
    f.write(dup)
    f.write(" ".join([str(x) for x in aa])+'\n')

    l1[ind]=max(l1)+1
#    whichfir.append(dup)


#f.write(str(lib))
#for i in
#print(lib)
#for i in whichfir:
#    print(i)
for i in libsend:
    print(i)

#    for i in range(func[ind][0]):
#        up_books.extend([])

f.flush()
f.close()