# Given an integer array find the sub array with the largest sum and return its sum
# kadene's Algorithm
# l=[-2,1,-3,4,-1,2,1,-5,4]
# s=[]
# for i in range(0,len(l)):
#     print(l[i])

# Maximum Separation [5,4,-1,7,8]

# str="aaabccccddd"
# x=0
# y=0
# z=0
# w=0
# l=[]
# for i in str:
#     if i =='a' :
#         x+=1
#     if i=='b':
#         y+=1
#     if i=='c':
#         w+=1
#     if i=='d':
#         z+=1
# print("a",x)
# print("b",y)
# print("c",w)
# print("d",z)
#
# #


n=int(input())
l=[]
for i in range(0,n):
    x=int(input())
    l.append(x)
mul=1
for p in l:
    mul=mul*p

print(mul)



