import re

with open('test.txt', 'r') as fh:
    lines = fh.readlines()
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

ip_list = []
for line in lines:
    match = pattern.search(line)
    if match:
        ip_list.append(match.group())
print(ip_list)