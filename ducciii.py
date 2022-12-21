def duccii(*n):
    while True:
        yield n
        n=list(abs(n[i-1]-n[i]) for i in range(len(n)))
def ducci(*n):
    x=list()
    for n in duccii(*n):
        print(n)
        if n in x or list(n)==[0]:
            break
        l.append(n)
print(ducci(0,653,1854,4063))