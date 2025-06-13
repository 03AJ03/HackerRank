# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, k = input().split()
k = int(k)
S = sorted(s)
P = permutations(S, k)
for p in P:
    print(''.join(p))
