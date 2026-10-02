import numpy as np

array = np.array(
    [[1, 2, 3, 4],     # 0 
     [5, 6, 7, 8],     # 1
     [9, 10, 11, 12],  # 2
     [13, 14, 15, 16]  # 3
    ]
    #0  #1   #2   #3
)

# array[ start : end : step]

# row selection
print("\nRow slicing / Selection :")
print(array[0::3], "\n")

# column selection
print("\nColumn slicing / Selection :")
print(array[:, ::2 ], "\n")  #------ Step means every 2nd, 3rd ,.. nth column
print(array[:, ::-2 ], "\n") # starts from end

# Selecting a quadrant
print(array[2:, 2:], '\n') # bottom right
print(array[0:2, 0:2]) # top left