import numpy as np

# Scalar

# array = np.array([1, 2, 3, 4])

# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array ** 5)


# Vectorized math functs

# array = np.array([1.01, 2.5, 3.99])

# print(np.round(array))
# print(np.sqrt(array))
# print(np.floor(array)) # round down
# print(np.ceil(array)) # round up

# print(np.pi)


# Element wise arithmetic

# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])

# print(array1 - array2)
# print(array1 + array2)
# print(array1 * array2)
# print(array1 / array2)

# COmparison Operators

scores = np.array([91, 55, 100, 73, 82, 64])

scores [scores < 60] = 0
print(scores == 100)