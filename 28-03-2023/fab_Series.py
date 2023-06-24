# N=int(input())
# series=0.0
# for i in range(1,N+1):
#     series=series+(i/(i+1))
# print(round(series,2))

# N=int(input())
# series=0.0
# for i in range(1,N+1):
#     series=series+1/i
# print("Sum",1/(N+1))
import math

'''N=int(input())
s=0.0
flag=0
for i in range(1,N+1):
    s=s+pow(i,i)/i
print(s)'''

# wap t ot ake 3 digit inout let n=123 and print the num in rev order

'''n=input()
print(n[::-1])'''

'''N=int(input())
flag=N
while N>0:
    r=N%10
    print(r,end="")
    N=int(N//10)'''
'''
def fact(n):
    flag=1
    for i in range(1,n+1):
        flag=flag*i
    return flag
sum=0
N=int(input())
temp=N
while N>0:
    r=N%10
    x=fact(r)
    sum=sum+x
    N=int(N//10)
if sum==temp:
    print("Strong Number")
    print(sum)
else:
    print("Not a Strong Number")'''

# 1 1 2 3 5 8 13

'''N=int(input())
sum=0
l=[]
for i in range(0,N+1):
    if i==0 and i==1:
        l.append(i)
    else:
        sum=l[i]+l[i-1]
        l.append(sum)
print(l)'''

# hashing number
'''
N=int(input())
temp=N
s=0
while N>0:
    r=N%10
    s=s+r
    N=int(N//10)
if temp%s==0:
    print("Hashing NUmber")
else:
    print("No")'''


'''import random as r
x=r.randrange(0,7)
y=r.randrange(0,7)
print(x,y)
print(x+y)'''


'''str=input()
flag=0
l=[]
m=[]
s=[]
flag=0
k=0
for i in str:
    l.append(i)
    flag+=1
for i in range(0,flag):
    s.append(l[i])
    while l[i]!=l[i+1]:
        m.append(k)

print(m)'''

s=input()
i=input()
for x in s:
    if x.isupper()==True:
        print(x.casefold())
    elif x.islower()==True:
        print(x.capitalize())
