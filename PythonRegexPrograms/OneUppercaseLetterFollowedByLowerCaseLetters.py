import re
s = 'geeAkAA55of55gee4ksabc3Ar2x'
for match in re.finditer(r'[A-Z][a-z]+', s):
    print(match.group())