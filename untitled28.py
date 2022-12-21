p=int(input("enter position"))
r=int(input("enter range"))
p=p+r
count=1
while count<10:
    print(p)
    p=p+(r+1)%10
    count+=1
    