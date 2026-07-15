import numpy as np

dataset_1 = np.array([9, 10, 11])
dataset_2 = np.array([1, 10, 19])

mean_of_dataset_1 = np.mean(dataset_1)
mean_of_dataset_2 = np.mean(dataset_2)
print(mean_of_dataset_1) # 10
print(mean_of_dataset_2) # 10

# let's find out the deviation from the mean 
deviation_1 = dataset_1 - mean_of_dataset_1
print(deviation_1) # [-1. 0. 1]
deviation_2 = dataset_2 - mean_of_dataset_2
print(deviation_2) # [-9. 0. 9.]

# squaring the deviations 
squaring_1 = deviation_1 ** 2
print(squaring_1) # [1. 0. 1]

squaring_2 = deviation_2 ** 2
print(squaring_2) # [81. 0. 81]

# average of squared deviations 
variance_1 = np.mean(squaring_1)
print("Variance 1: ", variance_1)

variance_2 = np.mean(squaring_2)
print("Variance 2: ", variance_2)


# both of them has same mean but their variance is different