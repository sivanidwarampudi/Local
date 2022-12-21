def processArray(liste):
    count=0
    for iter in liste:
        if iter%2==0:
            print(iter)
            count=0
        else:
            count=count+1
            if count>=2:
                print(count)
            else:
                print(iter)
liste=[]
while True:
        inp=int(input())
        if inp==-1:
            break
        liste.append(inp)
processArray(liste)
