'''s=input()
for i in s:
    if i.isupper()==True:
        print(i.casefold(),end="")
    elif i.islower()==True:
        print(i.capitalize(),end="")'''
'''
V=int(input())
W=int(input())
cars=(W-(2*V))/2
bike=V-cars
print(cars,bike)'''

'''freq=['High','Low','High','High','High','High']'''


def max(arr):
    arr.sort()
    n=len(arr)
    return arr[n-1]*arr[n-2]*arr[n-3]

arr=list(map(int,input("").split(",")))
r=max(arr)
print(r)