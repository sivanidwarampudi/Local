#l=[tuple(str(x)) for x in input().split()]
#print(l)
n=int(input())
l=[int(x) for x in input().split()]
d={}
for i in l:
    d[i]=d.setdefault(i,l.count(i))
    print(d[i])