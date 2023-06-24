# n=int(input())
# i=int(input())
# x=str(bin(n))
# if x[pos+2]=='1':1256
#     print("Yes")
# else:
#     print("no")
# if (n>>i)&1==1:
#     print("Yes")
# else:
#     print("No")
# k=0
#
# x=int(input())
# y=str(bin(x))
# for i in y:
#     if i=='1':
#         k=k+1
# print(k)

n=int(input())
count=0
# while(n):
#     if (n%2!=0):
#         count+=1
#     n=n>>1
#
# print(count)


while(n):
    n=(n)&(n-1)
    count+=1

print(count)