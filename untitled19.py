s="my marks are 1010101"
sum=0
for e in s:
    if(e.isdigit()==True):
        sum=(sum*2)+int(e)
for e in s:
    if(e.isdigit()==False):
        print(e,end="")
    else:
        print(sum)
        break
    