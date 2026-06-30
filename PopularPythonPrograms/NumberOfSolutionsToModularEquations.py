import math
A = 21
B = 5

if A == B:
    print("For A =", A, "and B =", B, ", X can take infinitely many values greater than", A)

elif A < B:
    print("For A =", A, "and B =", B, ", X cannot take any value")

else:
    count = 0
    N = A - B
    limit = int(math.sqrt(N))

    for i in range(1, limit + 1):
        if N % i == 0:
            if i > B:
                count += 1
            if N // i != i and N // i > B:
                count += 1

    print("For A =", A, "and B =", B, ", X can take", count, "values")