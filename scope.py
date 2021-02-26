# #override outer variable 
# class Namespace:pass
# def outer():
#     ns= Namespace()
#     ns.var="Outer"
#     def inner():
#         ns.var="inner"
#         print (ns.var)
#     inner()
#     print(ns.var)
# outer()
# #override global variable in module level
# global_var="IAmGlobal"
# def test1():
#     global global_var
#     global_var="IAmInSider"
#     print(global_var)
# test1()
# print(global_var)

global_var="IAmGlobal"
def test1():
    global_var="IAmInSider" #same variable name with global
    print(global_var)
test1()
print(global_var)


