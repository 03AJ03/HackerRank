# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

x=[15,12,8,8,7,7,7,6,5,3]
y=[10,25,17,11,13,17,20,13,9,15]

n = len(x)
mean_x = sum(x) / n
mean_y = sum(y) / n
numerator = 0
sum_x = 0
sum_y = 0
for i in range(n):
    dx = x[i] - mean_x
    dy = y[i] - mean_y
    numerator += dx * dy
    sum_x += dx ** 2
    sum_y += dy ** 2

r = numerator / math.sqrt(sum_x * sum_y)
print(r)
