# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
matches = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])', s)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)
