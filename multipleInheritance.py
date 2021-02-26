# class A:
#     x=100

# class B(A):
#     pass

# class C(A):
#     x=50

# class D(B,C):
#     pass

# obj=D()
# print(obj.x)
# print(D.__mro__)
# class A(object):
#     def dothis(self):
#         print('Doing this in A')

# class B(A):
#     pass

# class C(object):
#     def dothis(self):
#         print('Doing this in C')

# class D(B, C):
#     pass

# d_instance = D()
# d_instance.dothis()
# # METHOD RESOLUTION ORDER
# print(D.mro())

class A(object):
	x=100
	
class B(A):
	pass

class C(A):
	x=50
	
class D(B,C):
	pass

obj=D()
print(obj.x)
