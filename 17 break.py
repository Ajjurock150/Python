"""av=5
x=int(input("Enter no.of candies you want:"))

for i in range(1,x+1):
    
    if x<av:
        print("Candy",i)
        i=i+1
    else:
     print("No stock")
     break"""
#2 example


for j in range(1,101):
    if j % 3 == 0 :
        continue
    print(j)