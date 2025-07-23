# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X=map(int,input().split( ))
marks=[]
for _ in range(X):
    marks.append(list(map(float, input().split())))
    
av=zip(*marks)
for Stmarks in av:
    avg = sum(Stmarks) / X
    print(f"{avg:.1f}")
