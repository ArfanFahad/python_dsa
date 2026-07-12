import numpy as np

dataset_1 = [9, 10, 11]
dataset_2 = [1, 10, 19]

mean_of_dataset_1 = np.mean(dataset_1)
mean_of_dataset_2 = np.mean(dataset_2)
print(mean_of_dataset_1) # 10
print(mean_of_dataset_2) # 10

# let's find out the deviation from the mean 
deviation_1 = mean_of_dataset_1 - dataset_1
print(deviation_1)
deviation_2 = mean_of_dataset_2 - dataset_2
print(deviation_2)

# squaring the deviations 
squaring_1 = deviation_1 * deviation_1
print(squaring_1)
squaring_2 = deviation_2 * deviation_2
print(squaring_2)

# average of squared deviations 
average_of_sq_deviations_1 = f"{np.mean(squaring_1):.2f}"
print("Variance 1: ", average_of_sq_deviations_1)
average_of_sq_deviations_2 = f"{np.mean(squaring_2)}"
print("Variance 2: ", average_of_sq_deviations_2)


# both of them has same mean but their variance is different