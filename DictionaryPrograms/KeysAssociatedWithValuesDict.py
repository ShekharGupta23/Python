d = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]}

res = {}
for key, vals in d.items():
    for v in vals:
        if v in res:
            res[v].append(key)
        else:
            res[v] = [key]
print( res)