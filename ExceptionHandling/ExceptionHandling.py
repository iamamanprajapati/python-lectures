# WAP to find division of two numbers

try:
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    z = x/y
    print("result = ", z)
except ValueError:
    print("please enter numbers only...")
except ZeroDivisionError:
    print("You could not devided by zero...")
finally:
    print("this is finally block...")
