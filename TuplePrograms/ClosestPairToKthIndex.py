t = [(3, 4, 9), (5, 6, 7)]
tup = (1, 2, 5)
K = 3

min_diff, res = float('inf'), None
for idx, val in enumerate(t):
    diff = abs(val[K-1] - tup[K-1])
    if diff < min_diff:
        min_diff, res = diff, idx

print(t[res])