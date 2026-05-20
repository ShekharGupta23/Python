a = ['bat', 'nat', 'tan', 'ate', 'eat', 'tea']
res = {}

for word in a:
    key = ''.join(sorted(word))  
    res[key] = res.get(key, []) + [word]  

output = list(res.values())
print(output)