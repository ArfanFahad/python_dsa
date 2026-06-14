import numpy as np 

A = np.array([
    [1, 2],
    [2, 1],
    [121, 211]
])

rank = np.linalg.matrix_rank(A)

print(rank)