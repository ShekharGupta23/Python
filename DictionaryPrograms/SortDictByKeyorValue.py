d = {2: 56, 1: 2, 3: 323}
for k, v in sorted(d.items(), key=lambda item: item[1]):
    print((k, v), end=" ")