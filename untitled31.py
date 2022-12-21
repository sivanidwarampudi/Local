def flatten(l):
    nl=[]
    for x in l:
        if type(x)!=list:
            nl.append(x)
        else:
            nl.extend(flatten(x))
    return nl