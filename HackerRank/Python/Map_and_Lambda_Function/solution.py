cube = lambda x: x**3
def fibonacci(n):
    fib=[]
    a,b=0,1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib

