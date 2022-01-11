li=[5,1,4,1,1]
mx=0
num=0
for i in range(0,len(li)):
    m=li.count(li[i])
    if m>mx:
        mx=m
        num=li[i]
if(mx>len(li)//2):
    print("Max count=",mx,"and Number is:",num)
else:
    print("No majority element")
    
