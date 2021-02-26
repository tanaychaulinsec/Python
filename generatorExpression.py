

@profile
def list_comprehensions():
    
    l=sum[i*i for i in range(1000000)]
    print ("done")

    ##### this will take 71.000mb due to List comprehension


@profiler
def generator_expressions():
    val =sum(i*i for i in range(1000000))
    print("done")
    ##### this will take 41.000mb 


list_comprehensions()

