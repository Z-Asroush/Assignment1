name = input("enter your name:")
family = input("enter your family:")

a = float(input("enter score lesson 1:"))
b = float(input("enter score lesson 2:"))
c = float(input("enter score lesson 1:"))

A = (a+b+c)/3

if A>= 17:
    print("great")
if A < 17 and A>=12:
    print("normal")
if A < 12:
    print ("fail")