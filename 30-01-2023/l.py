# n=int(input())
# l1=[]
# l2=[]
# temp=[]
# max=float()
# for i in range(0,n):
#     for j in range(0,1):
#         name=input()
#         marks=float(input())
#         l2.append(name)
#         l2.append(marks)
#     l1.append(l2)
#     l2=[]
# for i in range(0,n):
#     for j in range(0,n):
#         if(l1[i][1]>l1[j][1]):
#             temp=l1[i]
#             l1[i]=l1[j]
#             l1[j]=temp
#         else:
#             continue
# for i in range (0,n):
#     for j in range(0,n):
#         if l1[i][1]>=l1[n-1][1] and l1[i][1]<l1[j][1]:
#             max=l1[i][1]
# for i in range (0,n):
#     if(l1[i][1]==max):
#         print(l1[i][0])