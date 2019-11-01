# hello.py


##Calculator

def add(x,y):
    z = x + y
    print()
    print("Answer:", z)

def sub(x,y):
    z = x -y
    print()
    print("Answer:", z)

def mult(x,y):
    z = x * y
    print()
    print("Answer:", z)

def expo(x,y):
    z = x ** y
    print()
    print("Answer:", z)

def div(x,y):
    z = x / y
    print()
    print("Answer:", z)

def mod(x,y):
    z = x % y
    print()
    print("Answer:", z)

def sqrts():
    from math import sqrt 
    x = float(input("What value would you want the square root of? "))
    y = sqrt(x)
    print()
    print("The answer is", y)

def fact():
    from math import factorial
    x = float(input("What value would you want the factorial of? "))
    y = factorial(x)
    print()
    print("The answer is", y)

def abval():
    from math import fabs
    x = float(input("What value would you want the absolute value of? "))
    y = fabs(x)
    print()
    print("The answer is" , y)

def loge():
    from math import log
    x = float(input("What value would you want the log of? "))
    base = float(input("What is the base value? "))
    y = log(x, base)
    print()
    print("The answer is" , y)

def cosine():
    from math import cos
    x = float(input("What value would you like the cosine of? "))
    y = cos(x)
    print()
    print("The answer is" , y)

def sine():
    from math import sin
    x = float(input("What value would you like the sine of? "))
    y = sin(x)
    print()
    print("The answer is" , y)

def tangent():
    from math import tan
    x = float(input("What value would you like the tangent of? "))
    y = tan(x)
    print("The answer is" , y)

def rad_to_deg():
    from math import degrees
    x = float(input("What radians do you want degrees of? "))
    y = degrees(x)
    print()
    print("The answer is" , y)

def deg_to_rad():
    from math import radians
    x = float(input("What degrees do you want radians of? "))
    y = radians(x)
    print()
    print("The answer is" , y)

def pie():
    from math import pi
    print()
    print(pi)

def nat():
    from math import e
    print()
    print(e)

def equ_cos():
    from math import cosh
    x = float(input("What value in cosine? "))
    y = cosh(x)
    print("The answer is" , y)
    

    

def Welcome():
    print("Welcome to the calculator function. Please choose an option below:")


def optionMenu():
    print()
    print("""1. Add
2. Subtract
3. Multiply
4. Exponents
5. Divide
6. Remainder
7. Square Root
8. Factorial
9. Absolute Value
10. Logs with a changable base
11. Cosine
12. Sine
13. Tangent
14. Radians to Degrees
15. Degrees to Radians
16. Pi
17. e
18. Hyperbolic Cosine
19. Exit""")

def explain():
    print("X value will be added to/subtracted to/multiplied to/divided by/to the power of/founder the remainder of Y")
    x = int(input("What is your x value?"))
    y = int(input("What is your y value?"))
    return x,y

def start():
    Welcome()
    choice = 1
    while choice != "19":
        optionMenu()
        choice = input("Choose 1-19: ")
        if choice == "1":
            x,y = explain()
            z = add(x,y)
        elif choice == "2":
            x,y = explain()
            z = sub(x,y)
        elif choice == "3":
            x,y = explain()
            z = mult(x,y)
        elif choice == "4":
            x,y = explain()
            z = expo(x,y)
        elif choice == "5":
            x,y = explain()
            z = div(x,y)
        elif choice == "6":
            x,y = explain()
            z = mod(x,y)
        elif choice == "7":
            sqrts()
        elif choice == "8":
            fact()
        elif choice == "9":
            abval()
        elif choice == "10":
            loge()
        elif choice == "11":
            cosine()
        elif choice == "12":
            sine()
        elif choice == "13":
            tangent()
        elif choice == "14":
            rad_to_deg()
        elif choice == "15":
            deg_to_rad()
        elif choice == "16":
            pie()
        elif choice == "17":
            nat()
        elif choice == "18":
            equ_cos()
        elif choice == "19":
            print()
        else:
            print("Please reenter")

start()
            
input("Press the enter key to exit")

