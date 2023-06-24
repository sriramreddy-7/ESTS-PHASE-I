def prime(n):
    k=0
    for i in
        if n%i==0:
            k=k+1
    if k==1:
        print('Prime Number')
    else:
        print('Not Prime Number')
n=int(input('Enter the Number: '))
prime(n)