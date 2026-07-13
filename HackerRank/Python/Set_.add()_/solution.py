# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
countries=set()
for _ in range(N):
    c=input()
    countries.add(c)
print(len(countries))
    
