# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
room_numbers = list(map(int, input().split()))

room_set = set(room_numbers)
total_sum = sum(room_set) * k
actual_sum = sum(room_numbers)

captain_room = (total_sum - actual_sum) // (k - 1)
print(captain_room)
