n=int(input("Enter the Limit: "))
l1=[]
for i in range(0,n):
    x=int(input('Enter List element :'))
    l1.append(x)
print(l1)
k=0
for i in range(0,len(l1)):
    k=l1.count(l1[i])
    if k==1:
        print('Repeated', l1[i], k, 'times')
    else:
        print('Repeated', l1[i], k, 'times')
        l1.remove(l1[i])
