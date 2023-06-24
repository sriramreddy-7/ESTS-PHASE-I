# class Computer:
#     def config(self):
#         print('Yes')
#
# dell=Computer()
# dell.config()

class Student():
    stname=input('Enter Student Name         : ')
    stroll=int(input('Enter Roll No          :'))
    stgrade=input('Enter the Branch of Student:')

    def toprint(self):
        stname=input('Enter Student Name         : ')
        print('Local Variable ',stname)
        print('Instance/Class Variable',self.stname)
        print('Instance/Class Variable', self.stroll)
        print('Instance/Class Variable', self.stgrade)

    def sf(self):
        print('Second Function!')

s1=Student()
s2=Student()
print(s1.stroll)
print(s1.stgrade)
print(s1.stname)

print('S2',s2.stname)
s1.toprint()
s2.toprint()
s2.sf()
# n=int(input('Enter the SIze: '))
# for i in range()






































