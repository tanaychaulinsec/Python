class classdecoretor(object):
    def __init__(self,func):
        self.func=func
    def __call__(self,*args):
        print("Someting before function call")
        self.func(*args)
        print("Someting after function call")
@classdecoretor        
def func1():
    print("Welcome to func1")

func1()
