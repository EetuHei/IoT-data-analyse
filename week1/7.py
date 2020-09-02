# Add the following two NumPy arrays and Modify a result array by calculating the square root of each element
import numpy as np
arrOne = np.array([[5, 6, 9], [21, 18, 27]])
arrTwo = np.array([[15, 33, 24], [4, 7, 1]])

result = arrOne + arrTwo
print(result)

for numbers in np.nditer(result, op_flags=['readwrite']):
    numbers[...] = numbers*numbers
print("result array after calculating the sqrt of all elements")
# [[ 400 1521 1089]
#  [ 625  625  784]]
print(result)
