l=[int(x) for x in input().split(" ")]
print("Original list {}".format(l))
d={l[i]:l.count(l[i]) for i in range(len(l))}
print("Printing count of each item {}".format(d))
