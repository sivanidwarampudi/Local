n = 3
  
list_1 = [1, 2, 3, 4, 5, 6] 
#list_2 = [1, 2, 3, 4, 5, 6] 
list_1 = (list_1[-n:] + list_1[:-n]) 
#list_2 = (list_1[n:] + list_1[:n]) 
print(list_1) 
#print(list_2)