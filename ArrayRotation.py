arr = [1, 2, 3, 4, 5, 6]
d = 2
arr[:] = arr[d:] + arr[:d]
print(arr)