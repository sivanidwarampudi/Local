lis=[]

while True:
    inp= int(input())

    if inp<0:
        break

    else:
        lis.append(inp)


def processArray(lis):
    count=0
    for x in lis:
        ind=lis.index(x)

        if x%2!=0:                             
            if ind!=len(lis)-1:                #  if not last element
                count=count+1         #count of odd sequence
                y=x                   #storing x for later use as x is removed from list
                lis.remove(x)
                lis.insert(ind,-1)    #replacing x with -1 as removing x changes entire list index structure, messing with for loop iteration
                #print('odd ',x, lis, count)  

            if ind==len(lis)-1 and count>1:     # if last element and count of odd > 1
                lis.remove(x)                   
                lis.append(count+1)            
                break

        elif x%2==0:            # if number = even
           # print('even ',x, lis, count)

            if count==1:        # if count of odd =1, keeping same number back from -1 to y 
                lis.remove(-1)
                lis.insert(ind-1,y)
                count=0
               # print('even count=1 ',x, lis, count)

            if count>1 :        # if count of odd >1, adding count element in list
                 lis.insert(ind-1,count)
                 count=0
                # print('even count>1 ',x, lis, count)

    while -1 in lis:            # removing all -1
           lis.remove(-1)

    return len(lis)

print('length of modified list ',processArray(lis))
print(lis)