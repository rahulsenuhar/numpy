import numpy as np

arr = np.array([12, 45, 67, 89, 34, 22, 90])
# basic function for each element
#addition, subtraction, multiply,division,

print("Addition", arr + 5)
print("subtraction", arr - 2)
print("multiply", arr * 5)
print("divition", arr / 5)

# Aggregate Functions

# Sum,min,max,mean,median,standard deviation,index of max, index of min,

arr = np.array([12, 45, 67, 89, 34, 22, 90])

print("Sum:", np.sum(arr))          # 359
print("Mean (Average):", np.mean(arr))   # 51.285
print("Median:", np.median(arr))    # 45.0
print("Standard Deviation:", np.std(arr)) # 29.050
print("Max:", np.max(arr))          # 90
print("Min:", np.min(arr))          # 12
print("Index of Max:", np.argmax(arr))  # 6
print("Index of Min:", np.argmin(arr))  # 0

# Matrix

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print("Element-wise Multiplication:\n", a * b)
print("Dot Product:\n", np.dot(a, b))   #dot and @ same
print("Matrix Multiplication (@):\n", a @ b)


# diagonal matrix

arr = np.arange(1,10).reshape(3,3)
print(np.diag(arr))