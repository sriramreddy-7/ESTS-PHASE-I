n1=int(input('Enter Number: '))
n2=int(input('Enter Number: '))
n3=int(input('Enter Number: '))
if n1>n2:
    if n1>n3:
        print(n1,'Greatest')
    else:
        print(n3, 'Greatest')
elif n2>n1:
    if n2>n3:
        print(n2, 'Greatest')
    else:
        print(n3, 'Greatest')
else:
    print(n3, 'Greatest')