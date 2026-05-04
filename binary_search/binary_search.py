arr = [12, 44, 56, 78, 134, 229, 313, 340]

def binary_search(arr, target):
    left_index = 0
    right_index = len(arr) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = arr[mid_index]

        if mid_value == target:
            return mid_index
        elif mid_value < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return None

print(binary_search(arr, 313))


