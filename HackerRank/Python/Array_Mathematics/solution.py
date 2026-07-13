import numpy
N,M=map(int,input().split())
A=[]
for _ in range (N):
    Arr1=list(map(int,input().split()))

for _ in range(N):
    Arr2=list(map(int,input().split()))
    
a=numpy.array(Arr1)
b=numpy.array(Arr2)
# print(numpy.add(a,b).reshape(1,-1))
# print (numpy.subtract(a, b).reshape(1,-1))
# print (numpy.multiply(a,b).reshape(1,-1))
# print(numpy.divide(a,b).reshape(1,-1))
# print(numpy.mod(a,b).reshape(1,-1))
# print(numpy.power(a,b).reshape(1,-1))
print((a+b).reshape(1,-1))
print((a-b).reshape(1,-1))
print((a*b).reshape(1,-1))
print((a//b).reshape(1,-1))
print((a%b).reshape(1,-1))
print((a**b).reshape(1,-1))
