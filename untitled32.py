def hanoi(n,fro,to,aux):
    if n==1:
        print("move %d from %s to %s using %s"%(n,fro,aux,to))
    else:
        hanoi(n-1,fro,aux,to)
        print("move %d from %s to %s using %s"%(n,fro,aux,to))
        hanoi(n-1,aux,to,fro)
hanoi(3,'a','b','c')