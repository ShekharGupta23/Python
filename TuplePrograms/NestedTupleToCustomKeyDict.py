a = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
res = []
for sub in a:
    res.append({'key': sub[0], 'value': sub[1], 'id': sub[2]})

print(str(res))