s = "Python is fun"
words = s.split()
res = ""

for word in reversed(words):
    res += word + " "

res = res.strip()
print(res)