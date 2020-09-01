# Following is the 2-D array. Print max from axis 0 and min from axis 1
import numpy as np
arr = np.array([[34,43,73],[82,22,12],[53,94,66]])

print("original array")
# [[34 43 73]
#  [82 22 12]
#  [53 94 66]]
print(arr)

minOfAxisxOne = np.amin(arr, 1)
print("amin of axis 1")
# [34 12 53]
print(minOfAxisxOne)

maxOfAxisOne = np.amax(arr, 0)
print("amax of axis 0")
# [82 94 73]
print(maxOfAxisOne)