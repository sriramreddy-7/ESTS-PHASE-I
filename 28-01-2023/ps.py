def num(n):
    l=[]
    p=1
    s=0
    for i in range(0,n):
        x=int(input('Enter the Number: '))
        l.append(x)

    for j in l:
        p=p*j
        s=s+j

    if p<750:
        print('Product is',p)
    else:
        print('Sum is',s)

n=int(input('Enter the Size: '))
num(n)