t1 = [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7)]
K = 1
res = []
for t in t1:
    if len(t) != K:
        res.append(t)
print(res)