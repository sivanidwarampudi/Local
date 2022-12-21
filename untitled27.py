#create a string such that which counts the freq of characters in previous string
#take a string enter a character and after how many times the chracter appeared after specified pos
#round table 10 kind of sweets 
str=input("enter string")
l="abcdefghijklmnopqrstuvwxyz"
i=0
for i in str: 
    if i in l: 
        l[i]+=1
    else: 
        l[i]=1
print(str[l]) 