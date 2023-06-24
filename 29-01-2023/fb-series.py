# def fabs(n):
#     sum=0
#     l=[]
#     for i in range(0,n):
#         if i==0 or i==1:
#             l.append(i)
#         else:
#             l.append(l[i-1]+l[i-2])
#     for i in l:
#         print(i)
# n=int(input('Enter the Number: '))
# fabs(n)


def fibo():

    for i in range(0,n):
        if i==0 or i==1:
            l.append(i)
        else:
            l.append(l[i-1]+l[i-2])

n=int(input("Enter the number:"))
l=[]
fibo()
for i in l:
    print(i,end=" ")
