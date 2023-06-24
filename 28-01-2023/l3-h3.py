def num(n):
    l=[]
    while n>0:
        k=int(n%10)
        l.append(k)
        n=int(n/10)
    l.sort()
    print('Highest Number :',max(l))
    print('Lowest Number  :',min(l))


n=int(input('Enter the Number: '))
num(n)

