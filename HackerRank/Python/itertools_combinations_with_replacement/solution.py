# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)
S = sorted(s)
P = combinations_with_replacement(S, k)
for p in P:
    print(''.join(p))
