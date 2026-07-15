import numpy as np

arr_1d = np.array([21, 38, 23, 98, 58])

#accessing first element 
print("first element: ", arr_1d[0])

#accessing last element 
print("last element: ", arr_1d[-1])

#----------------------------------------

#two dimensional array 
arr_2d = np.array([
#col:0   1   2
    [33, 87, 34], #row 0
    [73, 23, 97], #row 1
    [61, 20, 17], #row 2
])

#accessing the element in first row, first colum
print(arr_2d[0, 0])
#accessing 2nd element in the first row
print(arr_2d[0, 1])
#accessing first element in the 2nd row
print(arr_2d[1, 0])
#last item in the last column
print(arr_2d[-1, -1])

