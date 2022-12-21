def swap_case(s):
    a=""
    for l in s:
        if l.isupper()==True:
            a+=(l.lower())
        else:
            a+=(l.upper())
    return a
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)