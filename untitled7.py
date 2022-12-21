def checkSubarraySum(arr,n,k):
    sume = 0
    for i in range(0,k):
        sume+= arr[i]
        for j in range(k,n):
            sume=(sume+arr[j]-arr[j - k]) 
            return sume
if __name__=="__main__":
    n=int(input())
    k=int(input())
    for x in range(n):
        arr=set([int(x) for x in input().split()])

    
    
		