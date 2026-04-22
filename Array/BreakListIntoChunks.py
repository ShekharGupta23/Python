a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3  
res = [] 
for i in range(0, len(a), n):  # Slice list in steps of n
    res.append(a[i:i + n])

print(res)