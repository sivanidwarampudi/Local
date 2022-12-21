#top down and bottom up 2 approaches botup given below botup is also calledd tabulation
#bottom up approach in dynamic programming
d={}
d[0]=0
d[1]=1
def btfib(n):
    for i in range(2,n+1):
        r=d[i-1]+d[i-2]
        d[i]=r
    ret=d[n]
    print(d)
    return ret
if __name__=='__main__':
    import timeit
    n=int(input())
    start=timeit.default_timer()
    print(btfib(n))
    end=timeit.default_timer()
    print("Time taken in seconds is",end-start)

