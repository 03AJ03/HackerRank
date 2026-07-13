
import numpy as np

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

a = np.array(arr)
m=np.mean(a,axis=1)
v=np.var(a,axis=0)
print(m)
print(v)
print("{0:.11f}".format(np.std(a)))

