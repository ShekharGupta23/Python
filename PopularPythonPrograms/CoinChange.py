S = [1, 2, 3]
n = 4
t = [0] * (n + 1)
t[0] = 1

for coin in S:
    for i in range(coin, n + 1):
        t[i] += t[i - coin]

print(t[n])