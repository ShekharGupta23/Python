t1 = (4, 5)
t2 = (7, 8)
res = []

for ele1 in t1:
    for ele2 in t2:
        res.append((ele1, ele2))
        res.append((ele2, ele1))

print(res)