import re
s = "geeks for geeks makes learning fun"
res = "geeks"

if re.match(res, s):
    print("True")
else:
    print("False")