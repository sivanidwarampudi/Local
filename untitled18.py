l=[2,3,4,5,2,4,5,5,9,5]
l1=[]
d=[]
for i in l:
    if i in l1:
        d.append(i)
    if i not in l1:
        l1.append(i)  
print(l1)
print(d)

