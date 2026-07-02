import re
s = "abba"
pattern = r"^([a-z]).*\1$|^[a-z]$"

if re.fullmatch(pattern, s):
    print("Valid")
else:
    print("Invalid")