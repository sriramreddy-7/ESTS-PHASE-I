# import math
# n=int(input('Enter Number: '))
# l=[]
# while n>0:
#     k=int(n%10)
#     l.append(math.floor(k))
#     n = int(n / 10)
# l.reverse()
# for i in range(0,len(l)):
#     print(l[i])
import math
n=int(input('Enter Number: '))
l=[]
while n>0:
    k=int(n%10)
    l.append(k)
    n=int(n/10)
l.reverse()
for i in range(0,len(l)):
    print(l[i])