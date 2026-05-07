keys = ["name", "age", "city"]
values = ["Robin", 30, "New York"]
d = {}
for k, v in zip(keys, values):
    d[k] = v
print(d)