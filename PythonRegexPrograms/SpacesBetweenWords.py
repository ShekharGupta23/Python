import re
s = "GeeksForGeeks"
res = re.sub(r'(?<!^)(?=[A-Z])', ' ', s).lower()
print(res)