# given an array fo size n which contains elementsb o or 1 print sort the array
# l=[0,1,0,0,1,1,0,1,1]
# temp=0
# for i in range(0,len(l)):
#     for j in range(0,len(l)):
#         if l[i]<l[j]:
#             temp=l[j]
#             l[j]=l[i]
#             l[i]=temp
#         else:
#             continue
# print(l)
# l1=[]
# for i in range(0,len(l)):
#     if l[i]==0:
#         l1.append(l[i])
# for i in range(0,len(l)):
#     if l[i]==1:
#         l1.append(l[i])
# print(l1)

# l.sort()
#
# zero=0
# one=0
# for j in range(len(l)):
#     if l[j]==0:
#         zero=zero+1
#     elif l[j]==1:
#         one=one+1
#
# for i in range(zero):
#     l[i]=0
# for i in range(one):
#     l[i]=1
# print(l)

# 2 POINTER ALGORITHM
l=[0,1,0,0,1,1,0,1,1]
i=0
j=len(l)-1
while(i<j):
    if l[i]<l[j]:
        l[j],l[i]=l[i],l[j]
    i = i + 1
    j=j-1
    # else:
    #     # i=i+1
    #     # j=j-1
    #     continue


print(l)
#  given an array szie n whwre every number appaer tice execpt one
