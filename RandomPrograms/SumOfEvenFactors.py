import math
n = 18

if n % 2 != 0:
    print(0)
else:
    res = 1
    temp = n
    for i in range(2, int(math.sqrt(temp)) + 1):
        count = 0
        curr_sum = 1
        curr_term = 1
        while temp % i == 0:
            count += 1
            temp //= i
            if i == 2 and count == 1:
                curr_sum = 0
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if temp >= 2:
        res *= (1 + temp)
    print(res)