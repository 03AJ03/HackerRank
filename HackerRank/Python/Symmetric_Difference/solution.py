# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
a=set(map(int,input().split()))
N=int(input())
b=set(map(int,input().split()))
lis=sorted(a.union(b)-a.intersection(b))
for x in lis:
    print(x)
