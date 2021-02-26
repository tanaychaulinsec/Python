class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return Vector(self.a+ other.a,self.b+ other.b)
    def __repr__(self):
        return "Vector (%d %d)"%(self.a,self.b)

#driver
v1=Vector(4,5)
print(v1)
v2=Vector(6,15)
print(v2)
print(v1+v2)
print(v1.__class__)
print(v1.__class__.__class__)


