from array import *
vals=array('i',[2])
for i in vals:
    print(i) 
    newarr=array(vals.typecode ,( a for a in vals))
    for e in newarr:
        print(e)
