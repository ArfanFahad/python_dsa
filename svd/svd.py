# | User    | Avengers | Iron Man | Titanic | Notebook |
# | ------- | -------- | -------- | ------- | -------- |
# | Alice   | 5        | 4        | ?       | ?        |
# | Bob     | 4        | 5        | ?       | ?        |
# | Charlie | ?        | ?        | 5       | 4        |
# | David   | ?        | ?        | 4       | 5        |


import numpy as np

ratings = np.array([
    [5, 4, 0, 0],
    [4, 5, 0, 0],
    [0, 0, 5, 4],
    [0, 0, 4, 5]
])

U, S, VT = np.linalg.svd(ratings)

print("U: ")
print(U)

print("Singular Values: ")
print(S)

print("VT: ")
print(VT)