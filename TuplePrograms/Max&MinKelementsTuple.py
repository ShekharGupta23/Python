tup = (5, 20, 3, 7, 6, 8)
K = 2

l = sorted(tup)
mi, ma = [], []

for i, val in enumerate(l):
    if i < K:
        mi.append(val)
    if i >= len(l) - K:
        ma.append(val)

print(mi)
print(ma)