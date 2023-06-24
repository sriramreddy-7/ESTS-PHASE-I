# l=[1,2,3,4,5,7,8,5,4]
# print(l[::-1])
# print(l[:4])
# print(l[1:])
# print(l[-2])
# l=['V','E','R','Y','G','O','O','D','D','A','Y']
# print(l[4:8])
l=['hyd','vizag','chennai','vijayawada']
city=[]
for n in l:
    if "v" in n:
        city.append(n)
print(city)

l1=[2**x for x in range(2,10)]
print(l1)

l2=[a for a in range(100,201,20)]
print(l2)

l3=[1,2,3,4,5,6]
l4=[i for i in l3 if (i<5)]
print(l4)

