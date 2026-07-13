# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    
    command, _ = input().split()
    other_set = set(map(int, input().split()))
    
    getattr(A, command)(other_set)

print(sum(A))
