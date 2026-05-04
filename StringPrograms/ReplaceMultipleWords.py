s = "Geeksforgeeks is best for geeks and CS" 
li = ["best", "CS", "for"] 
k = "gfg"  

for word in li:
    s = s.replace(word, k)
print(s)