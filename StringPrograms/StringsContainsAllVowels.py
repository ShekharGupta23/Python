s = "education"
v = 'aeiou' 
a = set() 
for char in s.lower():
    if char in v: 
        a.add(char)  
    if len(a) == 5:  
        print("True")
        break
else:
    print("False")