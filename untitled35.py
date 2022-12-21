list=[x for x in input().split()]
freq={}
l=[]
for i in list:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for key,value in freq.items():
    