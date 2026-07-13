# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

def is_valid(email_address):
    
    pattern = r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email_address)

n = int(input())
for _ in range(n):
    full_input = input()
    name, addr = email.utils.parseaddr(full_input)
    
    if is_valid(addr):
        print(email.utils.formataddr((name, addr)))
