import random as r
n=''
k=0
x=r.randrange(1,100)
# print('System Generated Number:'x)
while n!=x:
    n = int(input('Enter any Number :'))
    k=k+1
    if n<x:
        print("Low")
    elif n>x:
        print('High')
    elif n>100 and n<0:
        print("Out of Range")
    else:
        print("Hurrah ! You Guessed Correct Answer!")
        print("You took",int(k),'Attempts')