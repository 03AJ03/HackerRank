# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
p=r'^[7,8,9]\d{9}$'
for _ in range(N):
    number=input()
    if re.match(p,number):
        print("YES")
    else:
        print("NO")
