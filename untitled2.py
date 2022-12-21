def pa(n):
    return str(n) == str(n)[::-1]
n=int(input(""))
if pa(n):
    print(n)
else:
    n1=n
    while not pa(n):
        n1=int(n1)+1
    print(n1)