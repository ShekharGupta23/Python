import numpy as np

a = ['a', 'b', 'c', 'd']
b = [3, 1, 4, 2]
res = [a[i] for i in np.argsort(b)]
print(res)