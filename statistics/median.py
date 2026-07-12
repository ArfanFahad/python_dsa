# finding median in tradition way 

values = [345, 25, 12, 10]

values.sort()
print(values)

n = len(values)

first_middle_index = n // 2 - 1
second_middle_index = n // 2 

print(values[first_middle_index])
print(values[second_middle_index])

median = (values[first_middle_index] + values[second_middle_index]) / 2
print(median)







