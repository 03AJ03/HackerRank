import numpy
N=int(input())
Arr1=[list(map(int,input().split()))for _ in range(N)]
Arr2=[list(map(int,input().split()))for _ in range(N)]
A=numpy.array(Arr1)
B=numpy.array(Arr2)
print(numpy.dot(A,B))

