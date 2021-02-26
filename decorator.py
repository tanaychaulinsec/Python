from datetime import datetime
def decoretor(func):
    def wrapped(*args):
        start=datetime.now()
        func(*args)
        end=datetime.now()
        print(end-start)
    return wrapped
@decoretor
def fact(n):
    fact=1
    for i in range(n,1,-1):
        fact=fact*i
    print (fact)
fact(6)