s1 = "apple"
s2 = "grape"

a = s1.lower()
b = s2.lower()
res = 0

for c in set(a):
    if c in b:
        res += 1

print(res)