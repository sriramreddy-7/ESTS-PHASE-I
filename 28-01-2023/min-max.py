def num():
    if n==999:
        print('Highest 3 Digit Number')
    elif n==100:
        print('Lowest 3 Digit Number')
    else:
       num()

n=int(input('Enter the Number: '))
num()