import numpy as np

# 1D Array Indexing

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])   # first element
print(arr[-1])  # last element

# 1D Array Slicing

OneD_arr =np.array([1,2,3,4,5])
print(OneD_arr)

#  print first two number
print("first two number: ",OneD_arr[: 2])

#  print last two number
print("last two number: ",OneD_arr[-2 :])

#  print every 2nd  number
print("Every two number: ",OneD_arr[:: 2])

# 2D Array Indexing

TwoD_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(TwoD_arr[0,0])

print("print 1 column: ",TwoD_arr[:,1 ])