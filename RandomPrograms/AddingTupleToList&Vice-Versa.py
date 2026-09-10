a = [1, 2, 3]
b = (4, 5) 
c = [6, 7] 

# add tuple to list a
a.extend(list(b))
print(a)

# add list to tuple b
temp_list = list(b)
temp_list.extend(c)
d = tuple(temp_list)
print(d)