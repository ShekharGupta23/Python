def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    left = arr[l:l + n1]
    right = arr[m + 1:m + 1 + n2]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

def iterativeMergeSort(arr):
    n = len(arr)
    curr_size = 1

    while curr_size < n:
        left_start = 0
        while left_start < n - 1:
            mid = min(left_start + curr_size - 1, n - 1)
            right_end = min(left_start + 2 * curr_size - 1, n - 1)
            merge(arr, left_start, mid, right_end)
            left_start += 2 * curr_size
        curr_size *= 2

arr = [12, 11, 13, 5, 6, 7]
print("Given array is:")
print(arr)

iterativeMergeSort(arr)
print("\nSorted array is:")
print(arr)