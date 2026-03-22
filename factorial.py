n = 6
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)