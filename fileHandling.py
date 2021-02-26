file1=open("input.txt","r")
file2=open("output.txt","w")
myList=[]
while 1:
    str1=file1.readline()
    if str1:
        myList=str1.split()
        file2.write(" ".join(myList))
        file2.write("\n")
        print( str1)
    else:
        break

file1.close()
file2.close()