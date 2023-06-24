def rainbow(c):
    if c=='V' or c=='v':
        print('Violet')
    elif c=='I' or c=='i':
        print('Indigio')
    elif c=='B' or c=='b':
        print('Blue')
    elif c=='G' or c=='g':
        print('Green')
    elif c=='Y' or c=='y':
        print('Yellow')
    elif c=='O' or c=='o':
        print('Orange')
    elif c=='R' or c=='r':
        print('Red')
    else:
        print('Not A Rainbow Color')

c = input('Enter the Chracter: ')
rainbow(c)