

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    def isempty(self):
        return(self.value==None)
    def append(self,v):
        if self.isempty():
            self.value=v
        elif self.next==None:
            nn=Node(v)
            self.next=nn
        else:
            (self.next).append(v)
    def show(self):
        if self.isempty():
            print("list empty")
            return 
        elif self.next==None:
            print(self.value)
            return
        else:
            print(self.value,end=' ')
            (self,next).show()
"""o/p:n=Node()

n.show()
list empty

n.append(11)

n.show()
11"""