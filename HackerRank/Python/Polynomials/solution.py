import numpy

Arr=list(map(float,input().split()))
x=float(input())
A=numpy.array(Arr)
print(numpy.polyval(A,x))

