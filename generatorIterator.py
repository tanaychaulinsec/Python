try:    
    def generator_exp(low,high):
        curr=low
        while curr<=high:
            yield curr
            curr+=1
except :
    print("Error")

c=generator_exp(3,9)
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())



