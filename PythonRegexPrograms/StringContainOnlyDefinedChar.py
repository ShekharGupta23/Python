import re
s = "abcXYZ!@#"
invalid_chars = re.findall(r"[^A-Za-z0-9]", s)

if invalid_chars:
    print("Invalid string:", invalid_chars)
else:
    print("Valid string")