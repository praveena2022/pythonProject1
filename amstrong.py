num=int(input())
order=len(str(num))
sum=0
temp=num
while temp>0:
    n=temp%10
    sum+=n**order
    temp=temp//10
if sum==num:
    print("yes")
else:
    print("No")

