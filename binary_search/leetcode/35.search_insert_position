nums = [1, 3, 5, 6]
target = 5

def bs(nums, target):
    left_index = 0
    right_index = len(nums) - 1
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = nums[mid_index]
        
        if mid_value == target:
            return mid_index
        elif mid_value < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

print(bs(nums, target))