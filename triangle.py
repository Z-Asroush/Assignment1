a =float( input("enter first number:"))
b =float( input("enter second number:"))
c = float (input("enter third number:"))

if a < b+c and  b < a+c and c < a+b:
     print("these numbers can form tiangle")
else: 
    print("these numbers can't form tiangle")
