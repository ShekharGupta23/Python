a, b = 8, 4

b1 = bin(a).count('1')
b2 = bin(b).count('1')

x = max(a.bit_length(), b.bit_length())
c1 = x - b1
c2 = x - b2

if b1 == b2 and c1 == c2:
    print("Yes")
else:
    print("No")