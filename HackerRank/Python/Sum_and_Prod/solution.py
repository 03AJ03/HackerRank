import numpy as np

N, M = map(int, input().split())

# Collect all N rows in a list
arr = [list(map(int, input().split())) for _ in range(N)]

# Convert to numpy array
a = np.array(arr)

# Sum along columns (axis=0)
column_sum = np.sum(a, axis=0)

# Product of the summed columns
product = np.prod(column_sum)

print(product)
