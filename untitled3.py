def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
if __name__=='__main__':
    import timeit
    n=int(input())
    start=timeit.default_timer()
    print(fib(n))
    end=timeit.default_timer()
    print("time taken in seconds",end-start)