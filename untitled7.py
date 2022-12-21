s1=input()
s2=input()
string=''
for i in range(len(s1)):
    if s1[i]==' ':
        continue
    for j in range(len(s2)):
      if s2[i]==' ':
          continue
      if s1[i]==s2[i]:
          pass
      else:
          string=string+s1[i]
          print(string)