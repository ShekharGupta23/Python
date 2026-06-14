import random

def bogo_sort(arr):
    while arr != sorted(arr):
        random.shuffle(arr)

arr = [3, 2, 4, 1, 0, 5]
bogo_sort(arr)
print("Sorted array:", *arr)