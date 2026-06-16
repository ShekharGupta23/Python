fp = "Myfile.txt"
n = 3

with open(fp, 'r') as f:
    text = f.read()

w1 = text.split()
w2 = [w for w in w1 if len(w) == n]

print(f"Words containing {n} characters:")
print(w2)