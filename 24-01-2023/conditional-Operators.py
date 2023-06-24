# cityname=input('Enter the City Name  : ')
# temp=int(input('Enter Temperature    : '))
# if temp>=40:
#     print(cityname,'is hot')
# elif temp>15 and temp<40:
#     print(cityname, 'is moderate')
# elif temp>=5 and temp<=15:
#     print(cityname, 'is cold')
# elif temp >= 0 and temp < 5:
#     print(cityname, 'is colder')
# else:
#     print(cityname, 'is coldest')
X,Y,s,T = [int(x) for x in input().split()]

print(sum([x+y<=T for x in range(X, X+s+1) for y in range(Y, Y+s+1)]))