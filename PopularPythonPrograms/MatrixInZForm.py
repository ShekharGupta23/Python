import numpy as np
arr = [[4, 5, 6, 8],
       [1, 2, 3, 1],
       [7, 8, 9, 4],
       [1, 8, 7, 5]]

m = np.array(arr)
print(*m[0], *np.diag(np.fliplr(m))[1:-1], *m[-1])