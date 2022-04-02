w = float(input("enter your weight(kg):"))
h = float(input("enter your height(m):"))

b = w / h**2

if b <=  18.5:
    print("your are underweight" )

if  b > 18.5 and b < 24.9: 
    print("you are normal")

if b >25 and b<29.9:
    print("you are overweight")

if b > 30 and b<34.9:
    print("you are obese")
if b>35:
    print("you are extremly obese")     