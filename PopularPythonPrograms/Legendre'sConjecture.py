import math
n = 10
for i in range(n*n, (n+1)*(n+1)):
    if i > 1:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            print(i)