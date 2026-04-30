s1 = "Geeks for Geeks"
s2 = "Learning from Geeks for Geeks"
words = (s1 + " " + s2).split()

res = []
for word in words:
    if words.count(word) == 1:
        res.append(word)

print(res)