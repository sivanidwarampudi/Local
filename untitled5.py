s1=input()
s2=input()
for i in range(len(s1)):
    for i in range(len(s2)):
        if s1[i]==s2[i]:
            print(s1[i])
        else:
            print("match not found")