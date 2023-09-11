"""def pattern():
    symbol=input("Enter symbol:")
    rows=int(input("Enter how many rows:"))
    columns=int(input("Enter columns:"))
    
    for i in range(1,rows+1):
        print(symbol *columns)
pattern()        
"""

'''for i in range(4):
    for j in range(i+1):
        print("# ",end="")
    print()    
    '''
    
for p in range(4):
    for q in range(4-p):
        print("# ",end="")
    print()     