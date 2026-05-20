s = "geeksforgeeks"
k = 3

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

res = []
for ch in s:
    if freq[ch] == 1:
        res.append(ch)

print(res[k - 1] if k <= len(res) else None)