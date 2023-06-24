#Passing Arguments To a function

'''def sum(n1,n2):
    print(n1,'+',n2,'=',n1+n2)

n1=int(input('Enter a Nummber :'))
n2=int(input('Enter a Nummber :'))
sum(n1,n2)'''

#Passing Arguments To a function with return type

def sum(n1,n2):
    return n1+n2

n1=int(input('Enter a Number :'))
n2=int(input('Enter a Number :'))

print(n1,'+',n2,'=',sum(n1,n2))

