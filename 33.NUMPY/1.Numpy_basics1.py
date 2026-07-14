"""What is numpy?

NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.


At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types

### Numpy Arrays Vs Python Sequences

- NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.

- The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory.

- NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.

- A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays.

### Creating Numpy Arrays
"""

# np.array
import numpy as np

# Create a 1D array from a Python list
# Output: [1 2 3]
print(np.array([1, 2, 3]))

# Create a 2D array with rows and columns
# Output:
# [[1 2 3]
#  [4 5 6]]
print(np.array([[1, 2, 3], [4, 5, 6]]))

# Create a 3D array with nested lists
# Output:
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]
print(np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]))

# Use dtype to control the data type of the array
# Output: [1. 2. 3.]
print(np.array([1, 2, 3], dtype=float))

# np.arange creates values with a step size
# Output: [1 3 5 7 9]
print(np.arange(1, 11, 2))

# Reshape a 1D sequence into a multi-dimensional array
# Output: a 4D array of shape (2, 2, 2, 2)
print(np.arange(16).reshape(2, 2, 2, 2))

# np.ones creates an array filled with ones
# Output: a 3x4 array of ones
print(np.ones((3, 4)))

# np.zeros creates an array filled with zeros
# Output: a 3x4 array of zeros
print(np.zeros((3, 4)))

# np.random creates random values between 0 and 1
# Output: random values in a 3x4 array
print(np.random.random((3, 4)))

# np.linspace creates evenly spaced values between two numbers
# Output: evenly spaced integers between -10 and 1
print(np.linspace(-10, 1, 10, dtype=int))

# np.identity creates an identity matrix
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
print(np.identity(3))

# Array attributes help us inspect the structure and type of an array.

a1 = np.arange(10, dtype=np.int32)
a2 = np.arange(12, dtype=float).reshape(3, 4)
a3 = np.arange(8).reshape(2, 2, 2)

# Output: a 3D array of shape (2, 2, 2)
print(a3)

# ndim shows the number of dimensions
# Output: 3
print(a3.ndim)

# shape shows the size of each dimension
# Output: (2, 2, 2)
print(a3.shape)
print(a3)

# size shows the total number of elements
# Output: 8
print(a3.size)
print(a3)

# itemsize shows the size of each element in bytes
# Output: 8 (on most systems)
print(a3.itemsize)

# dtype shows the data type used by the array
# Output: int32
print(a1.dtype)
# Output: float64
print(a2.dtype)
# Output: int64
print(a3.dtype)

# Changing Datatype
# astype converts an array to a different data type
# Output: the same values stored as int32
print(a3.astype(np.int32))

# Array operations help us perform math on arrays efficiently.
a1 = np.arange(12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(3, 4)

# Output: a 3x4 array
print(a2)

# Scalar operations apply the same rule to every element
# Output: each element squared
print(a1**2)

# Relational operations compare elements
# Output: True/False values
print(a2 == 15)

# Vector operations work element-wise between two arrays
# Output: element-wise power values
print(a1**a2)

# Array functions make common calculations easier.
a1 = np.random.random((3, 3))
a1 = np.round(a1 * 100)
# Output: a 3x3 array of rounded values
print(a1)

# max/min/sum/prod can be applied across rows or columns
# 0 -> column-wise and 1 -> row-wise
# Output: product values across each column
print(np.prod(a1, axis=0))

# mean/median/std/var measure the spread of values
# Output: variance for each row
print(np.var(a1, axis=1))

# trigonometric functions work on each element
# Output: sine values of the array
print(np.sin(a1))

# dot product is used for matrix multiplication
# Output: a 3x3 result matrix
print(np.dot(np.arange(12).reshape(3, 4), np.arange(12, 24).reshape(4, 3)))

# exp gives the exponential of each element
# Output: exponential values
print(np.exp(a1))

# round/floor/ceil help us control number formatting
# Output: rounded-up values
print(np.ceil(np.random.random((2, 3)) * 100))

# Indexing and slicing let us access parts of an array.
a1 = np.arange(10)
a2 = np.arange(12).reshape(3, 4)
a3 = np.arange(8).reshape(2, 2, 2)

# Output: a 3D array
print(a3)

# Output: a 1D array
print(a1)

# Output: a 2D array
print(a2)

# Access one specific element from a 2D array
# Output: 4
print(a2[1, 0])

# Access one specific element from a 3D array
# Output: 5
print(a3[1, 0, 1])

# Output: 6
print(a3[1, 1, 0])

# Output: the 1D array again
print(a1)

# Slice values with a step size
# Output: [2 4]
print(a1[2:5:2])

# Output: a sliced 2D view
print(a2[0:2, 1::2])

# Output: another sliced 2D view
print(a2[::2, 1::2])

# Output: [0 3 6 9]
print(a2[1, ::3])

# Output: first row of the array
print(a2[0, :])

# Output: third column of the array
print(a2[:, 2])

# Output: a sub-array from rows 1 onward and columns 1 to 3
print(a2[1:, 1:3])

a3 = np.arange(27).reshape(3, 3, 3)
# Output: a 3x3x3 array
print(a3)

# Output: a selected pattern from the 3D array
print(a3[::2, 0, ::2])

# Output: a slice from the last block
print(a3[2, 1:, 1:])

# Output: the middle row of the first block
print(a3[0, 1, :])

# Iterating lets us visit each element or each row.
print(a1)

for i in a1:
    print(i)

print(a2)

for i in a2:
    print(i)

print(a3)

for i in a3:
    print(i)

for i in np.nditer(a3):
    print(i)

# Reshaping changes the layout of the array without changing its data.

# transpose flips the dimensions
# Output: a transposed array
print(np.transpose(a2))
print(a2.T)

# ravel flatten the array into a 1D array
# Output: a flattened 1D version
print(a3.ravel())

a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
print(a5)

# Stacking combines arrays together.

# horizontal stacking joins arrays side by side
# Output: arrays combined horizontally
print(np.hstack((a4, a5)))

# Vertical stacking joins arrays one above another
# Output: arrays combined vertically
print(np.vstack((a4, a5)))

# Splitting divides one array into smaller parts.

# horizontal splitting divides the array by columns
# Output: split arrays along columns
print(np.hsplit(a4, 4))

# vertical splitting divides the array by rows
# Output: split arrays along rows
print(np.vsplit(a5, 3))
