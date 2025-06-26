# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N=int(input())
items = OrderedDict()

for _ in range(N):
    line = input().rsplit(' ', 1)
    item_name = line[0]
    price = int(line[1])
    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item, total_price in items.items():
    print(f"{item} {total_price}")
