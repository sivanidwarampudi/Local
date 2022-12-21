def gridpath(i,j):
    if i==0 and j==0:
        return 1
    elif i==0:
        return gridpath(0,j-1)
    elif j==0:
        return gridpath(i-1,0)       
    elif i==4 and j==4:
        return 0
    else:
        return gridpath(i-1,j)+gridpath(i,j-1)
d={}
d[(0,0)]=1
def btpath(i,j):
    for c in range(1,j+1):
        d[(0,c)]=1
    for r in range(1,i+1):
        d[(r,0)]=1
    for c in range(1,j+1):
        for r in range(1,i+1):
            d[(r,c)]=d[(r-1,c)]+d[(r,c-1)]
    return d[(i,j)]
if __name__=="__main__":
    i=int(input())
    j=int(input())
    import timeit
    start=timeit.default_timer()
    print(btpath(i,j))
    end=timeit.default_timer()
    print("Time taken in seconds is",end-start)    

        
    
    
    


