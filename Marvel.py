x=[1,2,3,4,5,6]
y=list(map(lambda u:u*5,filter(lambda v: v%2==0,x)))
print("{}".format(y))
print(x,y)
