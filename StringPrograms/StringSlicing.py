s = "GeeksforGeeks"
d = 2
n = len(s)

# Left Rotation
left = ""
for i in range(d, n):
    left += s[i]
for i in range(d):
    left += s[i]

# Right Rotation
right = ""
for i in range(n - d, n):
    right += s[i]
for i in range(n - d):
    right += s[i]

print("Left Rotation:", left)
print("Right Rotation:", right)