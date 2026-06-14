import numpy as np

ages = np.array([18, 22, 25, 20, 30])

print("Shape: ", ages.shape)
print("Data type: ", ages.dtype)
print("First age: ", ages[0])
print("Last age: ", ages[-1])
print("Sum of ages: ", ages.sum())
print("Average age: ", ages.mean())
print("Oldest age: ", ages.max())
print("Youngest age: ", ages.min())
print("Ages after adding 1 year to everyone: ", ages + 1)
print("Ages after doubling them: ", ages * 2)
