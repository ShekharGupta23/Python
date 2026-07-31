a, b = 10, 15
while b:
    a, b = b, a % b

print("GCD is", a)