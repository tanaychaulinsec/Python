class Delegation:
    def __init__(self,a):
        self.a=a
    def append(self,s):
        self.a.append(s.upper())
    def __getattr__(self,name):
        return getattr(self.a,name)
 #driver

b=[1,2,3,4]
a=Delegation(b)
print(b)
a.append("sb")
print(b)
 
