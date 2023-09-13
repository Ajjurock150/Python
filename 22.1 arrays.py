from array import *

arr=array('I',[])

n=int(input("Enter length of array "))

for i in range(n):
    x=int(input("Enter next value:"))
    arr.append(x)
print(arr)


#search for array
val=int(input("Enter value to search:"))

k=0
for e in arr:
    if e == val:
        print("Found ",e)
        break
    