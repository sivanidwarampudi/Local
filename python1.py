salary=int(input("enter salary"))
joblevel=int(input("enter joblevel"))
if joblevel==3:
    print(salary+salary*0.15)
elif joblevel==4:
    print(salary+salary*0.7)
elif joblevel==5:
    print(salary+salary*0.5)
else:
    print(salary)