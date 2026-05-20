def sort_dict(t):
    if not t:
        return {}
    m1 = min(t.keys())
    s1 = sorted(t[m1])
    remaining = {k: v for k, v in t.items() if k != m1}
    return {m1: s1, **sort_dict(remaining)}

t = {'gfg': [7, 6, 3], 'is': [2, 10, 3], 'best': [19, 4]}
res = sort_dict(t)
print(res)