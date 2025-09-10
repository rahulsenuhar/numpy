import numpy as np

print("radha")

#  Creating 1D array 

arr_1d = np.array([1,3,5,6])
print(arr_1d)

#  Creating 2D array

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)

#  Creating Zerose array
Zerose_arr = np.zeros((2,2))
print("Zerose array 2 row and 2 column", Zerose_arr)

# Creating Ones array
Ones_arr = np.ones((2,3))
print("Ones array 2 x 3 Matrix", Ones_arr)

# Creating arange() array

arande_arr = np.arange(0,10,2)
print("arange array: 0 and 10 define rande and 2 define step",arande_arr)

# Creating linspace array
Linspace_arr = np.linspace(0,1,5)
print("5 numbers between 0 & 1\n",Linspace_arr)

# Identity matrix

idnt_arr = np.eye(3)
print("Identity Matrix\n",idnt_arr)

# array properties 
print("Properties of Array")
arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print("Dimension : ",arr.ndim)
print("shape : ",arr.shape)
print("Size : ",arr.size)
print("Type : ",arr.dtype)