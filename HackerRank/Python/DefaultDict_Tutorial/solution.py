# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
a= defaultdict(list)
n,m=map(int,input().split())
for i in range(1, n + 1):
    word=input()
    a[word].append(i)

for _ in range(m):
    b= input()
    if b in a:
        print(" ".join(map(str, a[b])))
    else:
        print(-1)
