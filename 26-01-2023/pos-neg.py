num=int(input('Enter the Number: '))
if num==0:
    print("Neither +ve or -ve Even")
elif num % 2 == 0:
    if num > 0:
        print('Positive and Even')
    else:
        print('Negative and Even')
else:
    if num>0:
        print('Positive and Odd')
    else:
        print('Negative and Odd')