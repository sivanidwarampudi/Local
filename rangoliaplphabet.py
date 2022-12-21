import string

alpha = string.ascii_lowercase

num = int(input())

def srange(n):
     list(range(n))+list(range(n-2,-1,-1))
     print(n)
     for i in srange(n):
         print('-'.join([alpha[n-j-1] for j in srange(i+1)]).center(4*(n-1)+1,'-'))