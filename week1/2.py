# Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np
x = np.array([1, 2, 3, 4])

# Original array:
# [1 2 3 4]
# Test if none of the elements of the said array is zero:
# True
# Original array:
# [0 1 2 3]
# Test if none of the elements of the said array is zero:
# False
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
x = np.array([0, 1, 2, 3])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
