import numpy
N,M,P=map(int,input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(M)]
print (numpy.concatenate((arr1, arr2), axis = 0))
