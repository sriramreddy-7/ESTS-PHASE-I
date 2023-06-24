import math
# a=15
# print(pow(2,3))
#
# n=int(input())
# k=n
# x=int(n/2)
# for i in range(0,x):
#     if k==(pow(2,i)):
#         print("Yes")
# for  i in range(1,10):
#     print(i,"&",i-1,"=",i&i-1)
# this program takes O(1) time complexity !
# n=int(input())
# if(n&(n-1)==0):
#     print("Yes")
# else:
#     print("No")

# count=0
# n=int(input())
# while((1&n)!=1):
#     count+=1
#     n=n>>1
# print(count)
# n=int(input())
# k=0

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
#
#        k=k+1
#############
#i=1
# while(i<=n/i):
#     if(n%i==0):
#         if(i==n/i):
#             k=k+1
#         else:
#             k=k+2
#
#
# print('Count Value   :',k)


# l=int(input()).split(",")

# l=[8,5,8,6,1,5,3,1,2,4,7,8,9]
# k=0
# for i in l:
#     x=l.count(i)
#     while(x==1):
#         print(i)
#         break
##########]

# l=[8,5,8,6,1,5,3,1,2,4,7,8,9,10,20,25]
# for i in range(0,len(l)):
#     count=0
#     for j in range(0,len(l)):
#         if l[i]==l[j]:
#             count=count+1
#     if(count==1):
#         print(l[i])
#         break
        # for only one single repeated value
l=[8,5,8,6,1,5,3,1,2,4,7,8,9,10,20,25,567]

for i in range(0,len(l)):
    ans = l[i]
    ans=ans^l[i]

print(ans)

n=int(input())
for i in range(0,len())