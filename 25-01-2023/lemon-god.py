lemon=int(input('Enter the No.of Lemons: '))
print('Lemon Required: ',3*7)

if lemon==21:
    print('Requirement Satisfied:', 3 * 7)
    print('Surplus Lemons:',lemon-21)

elif lemon > 21 :
    print('Requirement  Satisfied:', 3 * 7)
    print('But Surplus lemons:', lemon - 21)

elif lemon<21 and lemon>=0:
    print('Requirement not Satisfied:', lemon)
    print('Lemons needed:', 21-lemon)

elif lemon < 0:
    print('Invalid Entry')
