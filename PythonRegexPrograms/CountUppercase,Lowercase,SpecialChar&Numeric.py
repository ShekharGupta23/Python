import re
s = "ThisIsGeeksforGeeks !, 123"

a = re.findall(r"[A-Z]", s)
b = re.findall(r"[a-z]", s)
c = re.findall(r"[0-9]", s)
d = re.findall(r"[, .!?]", s)  # includes space as a special character

print("No. of uppercase characters:", len(a))
print("No. of lowercase characters:", len(b))
print("No. of numerical characters:", len(c))
print("No. of special characters:", len(d))