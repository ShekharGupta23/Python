a = [(1, 2), (), (3, 4), (), (5,)]
res = [] 

for t in a:
    if t:
        res.append(t)
print(res)