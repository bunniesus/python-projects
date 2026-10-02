import numpy as np

# One dimensional array
array = np.array([1, 2, 3, 4])
print(array)
print(array.ndim)

# Multi dimensional array
#2D
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12]])
print(array)
print(array.ndim)

#3D
array = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                  [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L']],
                  [['P', 'Q', 'R', 'S'], [55, 66, 77, 88], [99, 30, 20, 40]]])
print(array)
print(array.ndim)
print(array.shape)
print("dept:", array.shape[0])
print("rows:", array.shape[1])
print("columns:", array.shape[2])

#chain indexing
#print(array[0][0][1], array[1][1][1])

#multi-D indexing
print(array[0,0,0], array[1,1,1])

word = array[1, 0, 0] + array[2, 0, 3] + array[2, 0, 3]
print(word)