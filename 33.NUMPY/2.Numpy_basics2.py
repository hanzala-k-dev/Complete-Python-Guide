"""Broadcasting
The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.

The smaller array is “broadcast” across the larger array so that they have compatible shapes.
"""

import numpy as np

# same shape
# Both arrays have the same shape, so they can be added directly.
a = np.arange(6).reshape(2, 3)
b = np.arange(6, 12).reshape(2, 3)

# Output: first 2x3 array
print(a)
# Output: second 2x3 array
print(b)

# Output: element-wise addition of both arrays
print(a + b)

# diff shape
# The second array has shape (1, 3), so it can be broadcast across the first array.
a = np.arange(6).reshape(2, 3)
b = np.arange(3).reshape(1, 3)

# Output: 2x3 array
print(a)
# Output: 1x3 array
print(b)

# Output: broadcasted addition result
print(a + b)

"""Broadcasting Rules
1. Make the two arrays have the same number of dimensions.

If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.
2. Make each dimension of the two arrays the same size.

If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised.."""

# More examples

# Example 1: shape (4, 3) with a 1D array of length 3
# The 1D array is broadcast across each row.
a = np.arange(12).reshape(4, 3)
b = np.arange(3)

# Output: 4x3 array
print(a)
# Output: 1D array of length 3
print(b)

# Output: broadcasted result
print(a + b)

# Example 2: shape (3, 4) with a 1D array of length 3
# This is incompatible because the last dimension 4 cannot be broadcast from 3.
a = np.arange(12).reshape(3, 4)
b = np.arange(3)

# Output: 3x4 array
print(a)
# Output: 1D array of length 3
print(b)

# Output: this example shows incompatible broadcasting
print(a + b)

# Example 3: shape (1, 3) and shape (3, 1)
# These shapes are compatible and produce a 3x3 result.
a = np.arange(3).reshape(1, 3)
b = np.arange(3).reshape(3, 1)

# Output: 1x3 array
print(a)
# Output: 3x1 array
print(b)

# Output: broadcasted addition result
print(a + b)

# Example 4: shape (1, 3) and shape (4, 1)
# These shapes are not compatible for broadcasting.
a = np.arange(3).reshape(1, 3)
b = np.arange(4).reshape(4, 1)

# Output: 1x3 array
print(a)
# Output: 4x1 array
print(b)

# Output: this will fail because the shapes are incompatible
print(a + b)

# Example 5: a single value array and a 2x2 array
# The single value is broadcast across the whole 2x2 array.
a = np.array([1])
# shape -> (1,1)
b = np.arange(4).reshape(2, 2)
# shape -> (2,2)

# Output: array containing [1]
print(a)
# Output: 2x2 array
print(b)

# Output: broadcasted addition result
print(a + b)

# Example 6: incompatible shapes (3, 4) and (4, 3)
# Broadcasting cannot align these shapes.
a = np.arange(12).reshape(3, 4)
b = np.arange(12).reshape(4, 3)

# Output: 3x4 array
print(a)
# Output: 4x3 array
print(b)

# Output: this will fail because the shapes are incompatible
print(a + b)

# Example 7: shape (4, 4) and shape (2, 2)
# A 2x2 array can be broadcast to a 4x4 array only if dimensions are compatible.
a = np.arange(16).reshape(4, 4)
b = np.arange(4).reshape(2, 2)

# Output: 4x4 array
print(a)
# Output: 2x2 array
print(b)

# Output: this will fail because the shapes are not compatible for broadcasting
print(a + b)


## Plotting Graphs

# plotting a 2D plot
# x = y
import matplotlib.pyplot as plt

# Create values from -10 to 10
x = np.linspace(-10, 10, 100)
y = x

# Output: a line plot showing the identity function
print(plt.plot(x, y))

# y = x^2
x = np.linspace(-10, 10, 100)
y = x**2

# Output: a curved line plot for the quadratic function
print(plt.plot(x, y))

# y = sin(x)
x = np.linspace(-10, 10, 100)
y = np.sin(x)

# Output: a sine wave plot
print(plt.plot(x, y))

# y = xlog(x)
x = np.linspace(-10, 10, 100)
y = x * np.log(x)

# Output: a logarithmic-style curve plot
print(plt.plot(x, y))

# sigmoid
x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))

# Output: a sigmoid curve plot
print(plt.plot(x, y))
