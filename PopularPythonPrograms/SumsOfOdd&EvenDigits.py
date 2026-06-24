n = 1212112
num_str = str(n)
odd_sum = 0
even_sum = 0

for i in range(len(num_str)):
    digit = int(num_str[i])
    if i % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

if abs(odd_sum - even_sum) == 0:
    print("Yes")
else:
    print("No")