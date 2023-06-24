# for i in range(15,56):
#     print(i)
#
# k=15
# while k<=55:
#     print(k)
#     k=k+1
import random as r

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

n = r.randint(num1, num2)

guess = int(input("Enter any number:"))

for i in range(num1, num2):

    if guess > n:
        print("Too high")
        guess = int(input("Enter any number:"))


    elif guess < n:
        print("Too Low")
        guess = int(input("Enter any number:"))

    else:
        break

print("You are right")