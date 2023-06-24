# get 3sides of trinagels as input and find out wether we can frame trinagle are not

def traingle(s1,s2,s3):
    if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
        print('Hurrah! You can form a Triangle.')
    else:
        print('Sorry ! You cannot form a Triangle.')

s1=int(input('Enter a Side :'))
s2=int(input('Enter a Side :'))
s3=int(input('Enter a Side :'))

traingle(s1,s2,s3)