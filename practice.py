
my_array = [20, 19, 31, 99, 920, 340, 21, 6, 44, 12]

def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    new_array = []
    
    for i in range(len(array)):
        smallest_number = find_smallest(array)
        new_array.append(array.pop(smallest_number))
    return new_array

print(selection_sort(my_array))


