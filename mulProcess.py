import random
from threading import Thread
from multiprocessing import Process
myList=[]
size=10000000
threads=2
for i in range(threads):
    myList.append([])
def func(count,mylist):
    for i in range(count):
        mylist.append(random.random())
def simple():
    for i in range(threads):
        func(size,myList[i])

#normal without using threading

#multiThreading
def multithreaded():
    jobs=[]
    for i in range(threads):
        thread=Thread(target=func,args=(size,myList[i]))
        jobs.append(thread)
    #start the threads
    for j in jobs:
        j.start()
    #ensure all thread have finished execution
    for j in jobs:
        j.join()


def multiprocessed():
    processes=[]
    for i in range(threads):
        p=Process(target=func,args=(size,myList[i]))
        processes.append(p)
    #start the processes
    for p in processes:
        p.start()
    #ensure all processes have finished execution
    for p in processes:
        p.join()

if __name__=="__main__":
    multiprocessed()  #faster
    # simple() #slower than multipreocess
    #thread() #slower than simple process
    



