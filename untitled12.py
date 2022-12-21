def recursiveCount(lst,key):
    if lst == []: 
        return 0
    if lst[0] == key:
        return 1 + recursiveCount(lst[1:],key)
    else:
        return 0 + recursiveCount(lst[1:],key)
print(recursiveCount(['a','b','a'],'a') )
