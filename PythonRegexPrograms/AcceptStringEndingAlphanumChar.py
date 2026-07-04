import re
text = "hello123"
pattern = r".*[A-Za-z0-9]$"

if re.fullmatch(pattern, text):
    print("Accept")
else:
    print("Discard")