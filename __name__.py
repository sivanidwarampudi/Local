"""from urllib.request import urlopen

def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        sw=[]
        for line in story:
            lw=line.decode('utf-8').split()
            for word in lw:
                sw.append(word)
    for word in sw:
        print(word)"""
from urllib.request import urlopen  
      
def fetch_words():
    s=urlopen('http://sixty-north.com/c/t.txt')
    sw=[]
    for l in s:
        lw=l.decode('utf-8').split()
        for w in lw:
            sw.append(w)
    s.close()
    for w in sw:
        print(w)
                