arr = [1, 3, 5, 7, 9, 11]
target = 4

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
    return -1

print(binary_search(arr, target))


