# # Problem: First Occurrence in a Sorted Array

# You are given a sorted array of integers and a target value.
# The array may contain duplicate elements.
# Your task is to:
# > Find the index of the first occurrence of the target value in the array.

# # Requirements
# * If the target exists multiple times, return the **leftmost (first) index**
# * If the target does not exist, return **-1**

# # Example 1
# Input:
# arr = [1, 2, 2, 2, 3, 4]
# target = 2

# Output:
# 1

# Explanation:
# The value `2` appears at indices 1, 2, and 3.
# The first occurrence is at index 1

arr = [1, 2, 2, 2, 3, 4]
target = 2

def bs_first_occurrence(arr, target):
    left_index = 0
    right_index = len(arr) - 1
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = arr[mid_index]
        
        if mid_value == target:

