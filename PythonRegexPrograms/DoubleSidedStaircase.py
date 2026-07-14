n = 10

for i in range(1, n + 1):
    k = i + 1 if i % 2 != 0 else i
    print(" " * (n - k) + (" * " * k))