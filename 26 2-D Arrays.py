from numpy import *
arr1=array([

[0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]

])
print(arr1)

#convert single to multi dimensional array
arr2=arr1.reshape(4,5)


#convert multi to single dimension array
arr4=array([

[4,5,2,4,5],[1,2,3,4,5]

])
arr5=arr4.flatten()
print (arr5)