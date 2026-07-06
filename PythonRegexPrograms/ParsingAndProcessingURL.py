import re  
s = 'https://www.geeksforgeeks.org/'

p = re.findall(r'(\w+)://', s)
print(p)

h = re.findall(r'://www.([\w\-.]+)', s)
print(h)