# Create a matrix for 4 students and 3 subjects:
# scores = np.array([
#     [85, 90, 88],
#     [70, 65, 80],
#     [95, 92, 96],
#     [60, 75, 70]
# ])

# Practice:
# Find shape
# Find dimensions
# Find total elements
# Get second student's marks
# Get all marks in subject 1
# Get the mark at row 2 column 1
# Average mark of each student
# Average mark of each subject
# Highest mark
# Lowest mark
# Add 5 to every mark
# Multiply all marks by 2



import numpy as np 

scores = np.array([
    [85, 90, 88],
    [70, 65, 80],
    [95, 92, 96],
    [60, 75, 70]
])

print("Shape: ", scores.shape)
print("Dimensions: ", scores.ndim)
print("Total elements: ", scores.size)
print("Get second student's marks: ", scores[1])
print("Get all marks in subject 1: ", scores[:,0])
print("Get the marks at row 2 column 1: ", scores[1, 0])

#         axis=1 →
#       ---------------->
#        [85 90 88]
# axis=0 [70 65 80]
#    ↓   [95 92 96]
#        [60 75 70]


# for row in scores:
#     print("axis=1", row)
    
# for col in scores.T:
#     print("axis=0", col)

# let's find out Average of each student with axis:

print("Average mark of each student: ", scores.mean(axis=1))
print("Average marks of each subject: ", scores.mean(axis=0))





