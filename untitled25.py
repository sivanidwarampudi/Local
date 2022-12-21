l=[1,3,5,89,56,10,9,8]
x=l[int(len(l)/2)]
count = 0
while x != 0: 
    x //= 10
    count+= 1
print(count) 
if count==2:  
    print(l[3:]+l[:3])
else:
  print("error")