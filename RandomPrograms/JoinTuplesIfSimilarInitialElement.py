from collections import defaultdict

t = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
mapp = defaultdict(list)

for k, v in t:
    mapp[k].append(v)

res = [(k, *v) for k, v in mapp.items()]
print(res)