import numpy as np
Arr1 = list(map(int, input().split()))
Arr2 = list(map(int, input().split()))
A = np.array(Arr1)
B = np.array(Arr2)

i=np.inner(A,B)
print(i)
print(np.outer(A,B))
