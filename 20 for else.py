

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

#Note: The else block will NOT be executed if the loop is stopped by a break statement.

nums=[12,17,85,56,29]
for i in nums:
        if i % 5 == 0:
            print(i)
            break
else:
    print("Not found")
        