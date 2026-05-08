arr = [156, 181, 6, 93, 47, 71, 251, 1, 10]

def find_smallest(arr):
	smallest = arr[0]
	smallest_index = 0

	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selection_sort(array):
    new_array = []
    
    for i in range(len(array)):
        smallest_number = find_smallest(array)
        new_array.append(array.pop(smallest_number))
    return new_array


print('Given Array: ', arr)
print('After selection sort: ', selection_sort(arr))