nums = [4,5,6,7,0,1,2]
target = 0

def rotate_sort(nums,target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid_index = (left + right) // 2
        
        if nums[left] <= nums[mid_index]:
            if nums[left] <= target < nums[mid_index]:
                right = mid_index - 1
            else:
                left = mid_index + 1
            return right
        
print(rotate_sort(nums, target))