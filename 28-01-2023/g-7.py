n=int(input("Enter the Size: "))
l=[]
for i in range(0,n):
    x=int(input("Enter the Number: "))
    l.append(x)
l.sort()
print('The Greatest No is ',max(l))
print('The Greatest No is ',l[n-1])