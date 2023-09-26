import numpy as np

# Sample NumPy array
sample_array = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24]
])

# Get the 3rd and 8th columns
columns_to_extract = [2, 7]  # 3rd column is index 2, and 8th column is index 7
result_array = sample_array[:, columns_to_extract]

# Print the result
print("Extracted columns:")
print(result_array)