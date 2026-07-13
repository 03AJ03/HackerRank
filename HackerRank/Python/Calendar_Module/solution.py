# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
import datetime
month, day, year = map(int, input().split())
date = datetime.date(year, month, day)
print(calendar.day_name[date.weekday()].upper())
