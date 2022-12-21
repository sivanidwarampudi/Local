avaone=int(input("enter available one coins"))
avafive=int(input("enter avaialble 5 coins"))
purchase=int(input("enter purchased amount"))
note=int(purchase/5)
five=note*5
onerem=purchase-five
one=onerem*1
if purchase>one+five:
    print("-1")
else:
    print(note)
    print(onerem)
