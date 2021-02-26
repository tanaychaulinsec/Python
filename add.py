import sys
def add(num1,num2):
    res=num1+num2
    print(res)

print(sys.argv[0])
add(int(sys.argv[1]),int(sys.argv[2]))