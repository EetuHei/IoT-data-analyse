# Sort following NumPy array
import numpy as np
arr = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

print("original array")
print(arr)

sortArrByRow = arr[:, arr[1, :].argsort()]
print("sort array by second row")
# [[73 43 34]
#  [12 22 82]
#  [66 94 53]]
print(sortArrByRow)

sortArrByColumn = arr[arr[:, 1].argsort()]
print("sort array by second column")
# [[82 22 12]
#  [34 43 73]
#  [53 94 66]]
print(sortArrByColumn)
