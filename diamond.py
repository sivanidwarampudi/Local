class base:
    nbc=0
    def callme(self):
        print("base class")
        base.nbc+=1
       

       

class leftsubclass(base):
    nlc=0
    def callme(self):
        base.callme(self)
        print("left subclas")
        leftsubclass.nlc+=1
       

class rightsubclass(base):
    nrc=0
    def callme(self):
        base.callme(self)
        print("right subclass")
        rightsubclass.nrc+=1
       

class multiple(leftsubclass,rightsubclass):
    ns=0
    def callme(self):
        leftsubclass.callme(self)
        rightsubclass.callme(self)
        print("sample class")
        multiple.ns+=1
m=multiple()
m.callme()
