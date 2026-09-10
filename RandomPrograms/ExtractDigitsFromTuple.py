t = [(15, 3), (3, 9), (1, 10), (99, 2)]

s = ''
for x in t:
    for y in x:
        s += str(y)
res = list(map(int, set(s)))
print(res)