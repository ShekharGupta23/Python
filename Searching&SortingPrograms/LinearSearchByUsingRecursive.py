def linear_search_rec(arr, x, i=0):
    if i == len(arr):
        return -1
    if arr[i] == x:
        return i
    return linear_search_rec(arr, x, i + 1)

arr = [10, 20, 30, 40, 50]
x = 30
res = linear_search_rec(arr, x)

if res != -1:
    print("Element", x, "found at index", res)
else:
    print("Element", x, "not found in the list")