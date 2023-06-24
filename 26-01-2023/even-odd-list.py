n=int(input("Enter the Limit: "))
l1=[]
for i in range(0,n):
    x=int(input('Enter List element :'))
    l1.append(x)
print(l1)
even=[]
odd=[]
for i in range(0,len(l1)):
    if l1[i]%2==0:
        even.append(l1[i])
    else:
        odd.append(l1[i])
print('Even')
for j in even:
    print(j)
print('------')
print('Odd')
for k in odd:
    print(k)
