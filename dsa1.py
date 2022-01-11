ar=[5,3,7,8,2,9]
print(ar)
n=len(ar)
for i in range(int(n/2)):
    c=ar[i]
    ar[i]=ar[n-i-1]
    ar[n-i-1]=c
print(ar)


