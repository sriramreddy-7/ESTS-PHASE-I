#  given an array szie n whwre every number appaer tice execpt one
l=[3,1,5,5,3,3,5,3,2,2,10]
# flag=0
# for i in range(len(l)):
#     flag=l.count(l[i])
#     if flag==1:
#         print(l[i])
########################################
for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if l[i]==l[j]:
            count+=1
    if count==1:
        print(l[i])

# bruteforce approach