import numpy as np 

A = np.array([
    [1, 2],
    [2, 4]
])

B = np.array([
    [1, 2],
    [3, 4]
])



result = np.matmul(A, B)

print(result)