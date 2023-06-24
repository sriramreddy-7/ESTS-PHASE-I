import math
a=float(input("Enter the Side 1: "))
b=float(input("Enter the Side 2: "))
c=float(input("Enter the Side 3: "))
s=(a+b+c)/2
x=s*(s-a)*(s-b)*(s-c)
print(x)
print("The Land Area is : ",(math.sqrt(x))/9)

# given a number print if it divibile by 15 fizz buzz ,print fizz div by 5,print buzz if div by 3