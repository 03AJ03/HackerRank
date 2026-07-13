# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    try:
        a, b = input().split()
        result = int(a) // int(b)
        print(result)
    except Exception as e:
        print("Error Code:", e)
