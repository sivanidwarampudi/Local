class Node:
   def __init__(self,value=None):
       self.value=value
       self.next=None
 

   
   def isempty(self):
       return (self.value==None)
   

   
       
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
           print('list is empty')
       elif self.next==None: #single value
           print(self.value)
           return
       else:
           print(self.value,end=' ')
           (self.next).show()


           
           
   def insert(self,v):
       if self.isempty():
           self.value=v
           return
       else:
           nn=Node(v)
           self.value,nn.value=nn.value,self.value
           self.next,nn.next=nn,self.next
           return



       
   def deletion(self,v):
       if self.isempty():
           print('list is empty')
           return
       elif self.value==v:
           if self.next==None:
               self.value=None
           else:
               #No it is not the firsset 4not=self  #A refferrence for self
               self.next=self.next.next
       t=self   #A refferrence for self
       while t.next!=None:
                   if t.next.value==v:
                       t.next=t.next.next
                       return
                   else:
                       t=t.next


                   
                       
   @classmethod
   def create_list(cls,l):
       n=Node()
       for i in l:
           n.append(i)
       return n

           
         
   
   @classmethod
   def concat(cls,l1,l2):
       temp=l1
       while temp.next!=None:
           temp=temp.next
       temp.next=l2
       
       
       
   
   
       
   @classmethod
   def reverse(cls,l):
       prev_node=None
       current_node=l
       while current_node is not None:
           n=current_node.next
           current_node.next=prev_node
           prev_node=current_node
           current_node=n
       return prev_node


 
   def count(self):
       if self.next==None:
           return 1
       else:
           return 1+self.next.count()
   def rotateright(self):
       t1=self
       
       while t1.next.next!=none:
           t1=t1.next
           t2=t1.next
           t1.next=None
           self.insertb(t2.value)
   def sort(self):
       t1=self
   
       
   
       
                
