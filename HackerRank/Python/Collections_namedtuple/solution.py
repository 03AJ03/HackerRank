# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N=int(input())
COL=input().split()
Student=namedtuple("Student",COL)
total_marks=0
for _ in range(N):
    record = input().split()
    student = Student(*record)
    total_marks += int(student.MARKS)
average = total_marks / N
print(f"{average:.2f}")
