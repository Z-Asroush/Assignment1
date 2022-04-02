import math

a = float(input("enter first number:"))
b = float(input("enter second number:"))
po = input("enter oprator:")

if po == "+":
    print(a+b)
if po == "-":
    print(a-b)
if po == "*":
    print(a*b)
if po=="/":
    if a!=0:
        print(a/b)     
    else:
        print("error")
if po=="radical":
   
    if a<0:
        y= math.sqrt (b)
        print("error and" , y)    
    if b<0:
        x= math.sqrt (a)
        print(x , "and error")     
    else:
        x= math.sqrt (a)
        y= math.sqrt (b)
        print(x , "and" , y ) 
if po=="sin":
    print(math.sin(math.radians(a)) , "and" , math.sin(math.radians(b)))
if po=="cos":
    print(math.cos(math.radians(a)) , "and" , math.cos(math.radians(b)))
if po=="tan":
    print(math.tan(math.radians(a)) , "and" , math.tan(math.radians(b)))    
if po=="cot":
    print(1/math.tan(math.radians(a)) , "and" , 1/math.tan(math.radians(b)))
if po=="!":
    print(math.factorial(int(a)) , "and" , math.factorial(int(b)))