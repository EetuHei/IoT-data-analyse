# Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
import numpy as np
arr = np.arange(100, 200, 10)
arr = arr.reshape(5, 2)

# [[100 110]
#  [120 130]
#  [140 150]
#  [160 170]
#  [180 190]]
print(arr)
