l=[23,12,10,3,8,20,23, 25,78]
t=min(l)
i=l.index(t)
r=l[i:]
s=l[:i]
p=sorted(l[i:],reverse=False)
q=sorted(l[:i],reverse=True)
if r==p and s==q:
    if len(r)==len(s):
        print("valley found")
    else:
        print("valley not found")
else:
    print("valley not found")