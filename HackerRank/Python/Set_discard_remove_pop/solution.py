# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().split()
    cmd=command[0]
    if cmd == "pop":
        s.remove(min(s))
    elif cmd == "remove":
        val = int(command[1])
        if val in s:  
            s.remove(val) 
    elif cmd == "discard":
        val = int(command[1])
        s.discard(val)

print(sum(s))
