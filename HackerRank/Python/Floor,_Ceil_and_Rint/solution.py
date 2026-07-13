import numpy
A=[]
Array=list(map(float,input().split()))
numpy.set_printoptions(legacy='1.13')
a=numpy.array(Array)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
