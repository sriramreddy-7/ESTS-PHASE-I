n=int(input("Enter the Size of  list: "))
l1=[]
s=0
for i in range(0,n):
    x=int(input('Enter List element :'))
    l1.append(x)
    s=s+l1[i]
if s%2==0 and s%5==0:
    print(s,'Divisible by 5 and 2')
else:
    print(s,'Not Divisible by 5 and 2')
