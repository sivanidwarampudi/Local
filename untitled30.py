def binary(n):
    if n==0 or n==1:
        return str(n)
    else:
        return binary(n//2)+str(n%2)
