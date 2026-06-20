n = 9
bits = n.bit_length()
is_palindrome = True

for i in range(bits // 2):
    if ((n >> i) & 1) != ((n >> (bits - i - 1)) & 1):
        is_palindrome = False
        break

print(is_palindrome)