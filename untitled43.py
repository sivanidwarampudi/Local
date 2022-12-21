def processArray(listf):
    count=0
    for i in listf:
        inde=listf.index(i)
        if i%2==0:                
            if inde!=len(listf)-1:  
                count=count+1    
                x=i            
                listf.remove(x)
                listf.insert(inde,-1)
            if inde==len(listf)-1 and count>1:    
                listf.remove(i)                  
                listf.append(count+1)            
                break
        elif i%2!=0:
            if count==1:        
                listf.remove(-1)
                listf.insert(inde-1,x)
                count=0            
            if count>1 :      
                 listf.insert(inde-1,count)
                 count=0
         
    while -1 in listf:
           listf.remove(-1)

    return len(listf)
listf=[]
while True:
    inp= int(input())
    if inp<0:
        break
    else:
        listf.append(inp)
processArray(listf)
for i in range(len(listf)):
    print(listf[i])