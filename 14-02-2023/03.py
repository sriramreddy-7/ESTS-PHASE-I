# class abc():
#     a=22
#     def qwe(self,l):
#         print(l)
#     def __init__(self,h):
#         print(h)
# #__init__ :constructor:double underscore is used
# ab=abc(500)
# print(ab)
# x=ab.qwe(900)
# print(x)


'''class number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num," is Even")
        else:
            print(num," is  Odd")'''

# n=number()
# n.even_odd(99)

#wap to seggrrate all the even num and odd num sep w.r.t to their lists by taking in consideration of class called number
# and a function using constuructor to assign the values of each num,print odd in one list and even in one list as given inputs
# into considertion  21,32,43,54,65

# class even_odd:
#         e=[]
#         o=[]
#         def __int__(self,i):
#             if self.i%2==0:
#                 self.e.append(i)
#             else:
#                 self.o.append(i)
#
# n=even_odd(21)
# n=even_odd(32)
# n=even_odd(43)
# n=even_odd(54)
# n=even_odd(89)

# print("Even:",even_odd.e)
# print("Odd :",even_odd.o)


#WAP THAT AS AS CLASS CIRCLE USE THE CLASS VARIBALE TO DEFINE TO DEFINE THE CONSTANT PI TILL THE 5 DIGITS
#TO CALCULATE AREA AND CIRUMFERENCE IN DIFFENRENT FUNCTIONS WITH SEPCIFIC RADIUS 7.5

'''
class circle:
    pi=3.14159
    def area(self,r):
        self.ar=self.pi*r*r
    def cirum(self,k):
        self.cr=2*self.pi*k



n=float(input("Enter the Radius :"))
obj=circle()
obj.area(n)
obj.cirum(n)
print("Area =",obj.ar)
print("Cirum=",obj.cr)'''


'''

1.__del__()  -deletes the scope autom 
2.__repr__() -string representation
3.__cmp__()  -compares two class objects
4.__len__()  length of a class object
5.__call__() the method lets a class to act like a function
6.__lt__ ,__le__ ,__eq__,__ne__,__gt__,__ge__ 
these are used to common 2 object 
7.  __hash__ it is used ti hash the objects
    __iter__ iterates over the subjects
    __getitem__ used for indexing  def __getitem__()
    __setitem__() def __setitem__(self,key,value) 

'''


# def hanoi(n,a,b,c):
#     if n>0:
#         hanoi(n-1,a,c,b)
#         if a:
#             c.append(a.pop())
#         hanoi(n-1,b,a,c)
#
# a=[1,2,3,4]
# b=[]
# c=[]
# hanoi(len(a),a,b,c)
# print(a,b,c)


