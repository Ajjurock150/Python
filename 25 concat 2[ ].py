from numpy import *
arr1 = array([1, 2, 3, 4])
arr2 = array([5, 6, 7, 8])
arr3 = array([9, 10, 11, 12])

print(type(arr1),type(arr2),type(arr3))
concatenated_array = concatenate([arr1, arr2, arr3])

print(concatenated_array)