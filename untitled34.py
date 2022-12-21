l=[x for x in input().split()]
count=0
for i in range(len(l)):
    a=l.count(i)
    count+=1
    print(l[i],count)