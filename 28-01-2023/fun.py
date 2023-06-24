# Functions Code Reusablity
# Pre-defined
# System Defined
# In-Built Functions

# def ksr(n):
#     print('This is Sriram DOB',n)
#
# n=input('Enter any Number: ')
# ksr(n)

#with argument without return value
# def sum(n1,n2):
#     print(n1, '-', n2, '=', n1-n2)
#
# n1=int(input('Enter the Value: '))
# n2=int(input('Enter the Value: '))
# sum(n1,n2)3

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))