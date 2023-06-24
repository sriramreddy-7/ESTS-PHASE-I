#WAP using fuction get a number as input as long as u r input is in blw to 75-100 .
# you should be promted to take number as input again
#if u r outside the boundry print it is over.
def num():
    n = int(input('Enter a Number :'))
    if n>75 and n<100:
       num()
    else:
        print('It is Over!')
num()

# l=[x for x in range(75,150)]
# print(l)
#if(75<x<100)
