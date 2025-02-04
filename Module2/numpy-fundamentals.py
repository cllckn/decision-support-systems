# numpy_examples.py
# Demonstrates various NumPy functionalities with explanations

import numpy as np

# 1. Initializing NumPy Arrays
print("=== 1. Initializing NumPy Arrays ===")

# initialize a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print("\n1D Array:")
print(arr1d)

# initialize a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr2d)

# initialize an array of zeros
zeros_arr = np.zeros((2, 3))
print("\nArray of Zeros:")
print(zeros_arr)

# initialize an array of ones
ones_arr = np.ones((3, 2))
print("\nArray of Ones:")
print(ones_arr)

# initialize an identity matrix
identity_matrix = np.eye(3)
print("\nIdentity Matrix:")
print(identity_matrix)

# initialize an array with a range
range_arr = np.arange(10)
print("\nArray with Range:")
print(range_arr)

# 2. Array Operations
print("\n=== 2. Array Operations ===")

# Element-wise addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a + b
print("\nElement-wise Addition:")
print(result)

# Element-wise multiplication
result = a * b
print("\nElement-wise Multiplication:")
print(result)

# Dot product
dot_product = np.dot(a, b)
print("\nDot Product:")
print(dot_product)

# Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
result = np.matmul(matrix_a, matrix_b)
print("\nMatrix Multiplication:")
print(result)

# 3. Array Indexing and Slicing
print("\n=== 3. Array Indexing and Slicing ===")

# Access elements of a 1D array
arr = np.array([10, 20, 30, 40, 50])
print("\nAccess Elements:")
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing a 1D array
print("\nSlicing:")
print("Elements from index 1 to 3:", arr[1:4])

# Access elements of a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nAccess Elements in 2D Array:")
print("First row, second column:", arr2d[0, 1])
print("All rows, second column:", arr2d[:, 1])

# 4. Array Reshaping
print("\n=== 4. Array Reshaping ===")

# Reshape a 1D array to 2D
arr = np.arange(9)
reshaped_arr = arr.reshape(3, 3)
print("\nReshaped Array:")
print(reshaped_arr)

# 5. Statistical Operations
print("\n=== 5. Statistical Operations ===")

# Calculate mean, median, and standard deviation
arr = np.array([1, 2, 3, 4, 5])
print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

# Sum and product of array elements
print("\nSum:", np.sum(arr))
print("Product:", np.prod(arr))

# 6. Random Number Generation
print("\n=== 6. Random Number Generation ===")

# Generate random numbers
random_arr = np.random.rand(3, 3)  # 3x3 array of random numbers between 0 and 1
print("\nRandom Array:")
print(random_arr)

# Generate random integers
random_int_arr = np.random.randint(1, 100, size=(3, 3))
print("\nRandom Integer Array:")
print(random_int_arr)

# 7. Linear Algebra
print("\n=== 7. Linear Algebra ===")

# Calculate the determinant of a matrix
matrix = np.array([[1, 2], [3, 4]])
det = np.linalg.det(matrix)
print("\nDeterminant of Matrix:")
print(det)

# Calculate the inverse of a matrix
inverse_matrix = np.linalg.inv(matrix)
print("\nInverse of Matrix:")
print(inverse_matrix)

# 8. Saving and Loading Arrays
print("\n=== 8. Saving and Loading Arrays ===")

# Save an array to a file
np.save('my_array.npy', arr)

# Load the array from the file
loaded_arr = np.load('my_array.npy')
print("\nLoaded Array:")
print(loaded_arr)
