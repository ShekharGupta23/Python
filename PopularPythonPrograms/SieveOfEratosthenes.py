import math
n = 30
prime = [True for _ in range(n + 1)]
prime[0], prime[1] = False, False

for p in range(2, int(math.sqrt(n)) + 1):
    if prime[p]:
        for i in range(p * p, n + 1, p):
            prime[i] = False

for i in range(2, n + 1):
    if prime[i]:
        print(i, end=" ")