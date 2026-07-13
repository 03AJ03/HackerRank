# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n, m = map(int, input().strip().split())
arr = np.array([list(map(int, input().strip().split())) for _ in range(n)])
print (np.transpose(arr))
print (arr.flatten())
