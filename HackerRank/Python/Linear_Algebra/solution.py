# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N=int(input())

arr=[list(map(float,input().split()))for _ in range(N)]
A=np.array(arr)
det=round(np.linalg.det(A),2)
print(det)
