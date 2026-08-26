n = 128
temp = n
flag = True

while temp > 0:
    digit = temp % 10
    if digit == 0 or n % digit != 0:
        flag = False
        break
    temp //= 10

if flag:
    print("Yes")
else:
    print("No")