t1 = [["Gfg", "good"], ["is", "for"], ["Best"]]
res = []
N = 0
while N < max(len(sub) for sub in t1):
    temp = ''
    for sub in t1:
        try:
            temp += sub[N]
        except IndexError:
            pass
    if temp:
        res.append(temp)
    N += 1
print( str(res))