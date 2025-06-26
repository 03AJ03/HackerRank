# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N=int(input())
d=deque()
for _ in range(N):
    l=input().split(" ",1)
    if(l[0]=="append"):
        d.append(l[1])
    elif(l[0]=="popleft"):
        d.popleft()
    elif(l[0]=="pop"):
        d.pop()
    elif(l[0]=="appendleft"):
        d.appendleft(l[1])
print(" ".join(d))
