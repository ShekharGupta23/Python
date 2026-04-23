import math
a = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
b = [ele for sub in a for ele in sub] 
res = math.prod(b)
print(res)