import numpy as np
#0-D array
"""arr = np.array(42)
print(arr)"""
#1-D array
"""arr=np.array([1,2,3,4])
print(arr)"""
#2-D array
"""arr = np.array([[1,2,3],[4,5,6]])
print(arr)"""
#3-D array
"""arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)"""
#1-D array
"""arr = np.array([1,2,3])
print(arr[0])
print(arr[2])"""
#2-D array
"""arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element on 1st row:',arr[0,1])
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element on 1st row:',arr[1,4])"""
#Slicing Arrays
#1-D array
"""arr= np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[4:])"""
#2-D array
"""arr= np.array([[1,2,3,4],[5,6,7,8]])
print(arr[0:1,0:2])
print(arr[0:2,0:2])
print(arr[0:2,1:3])
print(arr[0:2,2:])
print(arr[1:2,2:])
print(arr[0:2,1:])
print(arr[1:,1:])
print(arr[0:2,0:1])"""
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr[1:,0:])
print(arr[0:,0:3])
print(arr[1:3,0:2])
print(arr[0:,1:3])
print(arr[0:1,1:3])


