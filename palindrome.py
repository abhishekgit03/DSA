x=121
z=x
d=0
r=0
if(x<0):
    print(0)
else:
    while(x>0):
        d=x%10 
        r=r*10+d
        x=x//10
    if(r==z):
       print(1)

    else: 
        print(0)
    

