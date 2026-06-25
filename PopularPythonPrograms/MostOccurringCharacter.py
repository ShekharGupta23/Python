s = "geeksforgeeks"
a = []
b = []

for ch in s:
    if ch not in a:
        a.append(ch)
        b.append(s.count(ch))

res = max(b)
ele = a[b.index(res)]
print(ele, res)