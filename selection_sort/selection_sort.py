arr = [156, 181, 6, 93, 47, 71, 251, 1, 10]

def find_smallest(arr):
	smallest = arr[0]
	smallest_index = 0

	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	print("Given Array = ", arr)
	print("Smallest Index = ", smallest_index)
	print("Smallest number = ", smallest)

find_smallest(arr)
