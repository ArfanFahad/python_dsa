# Chapter 23: NumPy Fundamentals
# * Arrays
# * Dimensions
# * Shapes
# * Data Types
# * Indexing
# * Slicing


import numpy as np 

#1d array
vector = np.array([2, 3, 12, 42])
print("Dimension: ", vector.ndim)
print("Shape: ", vector.shape)
print("Data type: ", vector.dtype)
print("Size of the array: ", vector.size)