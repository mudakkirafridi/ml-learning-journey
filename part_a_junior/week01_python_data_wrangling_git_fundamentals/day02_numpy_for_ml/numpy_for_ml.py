import numpy as np

# =====================================================
# 1. Creating NumPy Arrays
# NumPy arrays store numerical data efficiently
# =====================================================

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1. Arrays")
print(arr1)
print(arr2)


# =====================================================
# 2. Shape, Dimensions, Size
# shape -> rows and columns
# ndim -> number of dimensions
# size -> total elements
# =====================================================

arr = np.array([[1,2,3],[4,5,6]])

print("\n2. Shape, Dimensions, Size")
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)


# =====================================================
# 3. Creating Special Arrays
# zeros, ones, random numbers
# =====================================================

zeros = np.zeros((2,3))
ones = np.ones((2,3))
random = np.random.rand(2,3)

print("\n3. Special Arrays")
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Random:\n", random)


# =====================================================
# 4. Indexing
# Access specific element
# =====================================================

arr = np.array([10,20,30,40])
matrix = np.array([[1,2,3],
                   [4,5,6]])

print("\n4. Indexing")
print(arr[0])
print(matrix[0,1])


# =====================================================
# 5. Slicing
# Extract part of array
# =====================================================

arr = np.array([1,2,3,4,5,6])

print("\n5. Slicing")
print(arr[1:4])

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(matrix[:,1])


# =====================================================
# 6. Vectorized Operations
# Perform operations on entire arrays
# =====================================================

arr = np.array([1,2,3,4])

print("\n6. Vectorized Operations")
print(arr + 5)
print(arr * 2)


# =====================================================
# 7. Mathematical Operations
# Important for ML calculations
# =====================================================

arr = np.array([1,2,3,4])

print("\n7. Mathematical Operations")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))


# =====================================================
# 8. Reshaping Arrays
# Change array shape
# =====================================================

arr = np.array([1,2,3,4,5,6])

reshaped = arr.reshape(2,3)

print("\n8. Reshaping")
print(reshaped)


# =====================================================
# 9. Broadcasting
# Automatic shape matching for operations
# =====================================================

arr = np.array([[1,2,3],
                [4,5,6]])

print("\n9. Broadcasting")
print(arr + 10)


# =====================================================
# 10. Dot Product (Important for ML)
# Used in linear algebra and neural networks
# =====================================================

a = np.array([1,2,3])
b = np.array([4,5,6])

dot = np.dot(a,b)

print("\n10. Dot Product")
print("Dot product:", dot)