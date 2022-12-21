td={}
td[0]=0
td[1]=1
def tdfib(n):
    if td.get(n,-1)!=-1:
        return td[n]
    else:
        td[n]=tdfib(n-1)+tdfib(n-2)
        return td[n]
if __name__=='__main__':
    import timeit
    n=int(input())
    start=timeit.default_timer()
    print(tdfib(n))
    end=timeit.default_timer()
    print("Time taken in seconds is",end-start)    
