s = "101010000111"
for char in s:
    if char not in '01':
        print("No")
        break
else:
    print("Yes")