# Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
import numpy as np
x = np.arange(10, 22).reshape(3, 4)

# [[10 11 12 13]
# [14 15 16 17]
# [18 19 20 21]]
print(x)
