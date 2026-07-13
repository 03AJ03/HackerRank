# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
arr=list(map(int,input().strip().split()))
np_array = np.array(arr).reshape(3, 3)
print (np_array)
