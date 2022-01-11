n=int(input("Enter a number:"))
i=5
x=0
while(i<=n):
    x=x+n//i
    i=i*5
print("Number of trailing zeroes in factorial=",x)