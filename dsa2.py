ar=[5,4,7,2,9]
max=ar[0]
min=ar[0]
for i in ar:
    if i<=min:
        min=i
    if i>=max:
        max=i
print("Max=",max)
print("Min=",min)