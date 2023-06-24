# l=[i for i in range(1,11)]
# l1=[]
# print(l)
# for k in range(0,len(l)):
#     if l[k]%2==0:
#         l1.append('Even')
#     else:
#         l1.append('Odd')
# print(l1)
# even=[i for i in l if(i%2==0)]
#
# odd=[i for i in l if(i%2!=0)]


#
# print(l)
# print(even)
# print(odd)
l=[i for i in range(1,11)]

l5=['even' if i%2==0 else 'odd' for i in l ]
print(l5)