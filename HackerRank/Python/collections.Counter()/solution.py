# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X=int(input())
L=list(map(int,input().split()))
inventory = Counter(L)
N=int(input())
sum=0
for _ in range (N):
    s,x=map(int,input().split())
    if inventory[s] > 0:
        sum += x
        inventory[s] -= 1
print(sum)
