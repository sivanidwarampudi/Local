x=input()
x=list(x)
l=[]
l.append(x[0])
count=0
for i in range(len(x)):
    if x[i]==l[len(l)-1]:
        count+=1
    else:
        l.insert(len(l)-1,count)
        l.append(x[i])
        count=1

l.insert(len(l)-1,count)
for i in l:
    print(i,end="")

