# n1=int(input('Enter the Number -1 : '))
# n2=int(input('Enter the Number -2 : '))
# try:
#     print('Resource is Open!')
#     print(n1/n2)
# except ZeroDivisionError as e:
#     print("Please note number can't be divided by zero",e)
#
# except ValueError as e:
#     print('Invalid Input',e)
#
# except Exception as e:
#     print("Other Error",e)
# finally:
#     print('Resource closed !')

# i=int(1)
# l=[]
# while i ==1:
#     x=input('Enter the Number: ')
#     if x is not None:
#         l.append(int(x))
#     else:
#         fun()
#
# def fun():
#     for i in l:
#         print(i)

x=int(input('Enter any Number: '))
if x%2!=0:
    raise Exception('X Shud be even Number!')
else:
    print('X is even Number...Correct')