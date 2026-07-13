# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
nums = list(map(int, input().split()))
pos=all(x>0 for x in nums)
pal=any(str(x)==str(x)[::-1] for x in nums)
print(pos and pal)
