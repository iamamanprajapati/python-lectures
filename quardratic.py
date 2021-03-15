# find the roots of quardratic equations
import math

a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of c: '))

discremenet = b*b - 4*a*c

if(discremenet < 0):
    print('discremenet is negative')
else:
    print('discremenet is positive')
    print("first root is : ", (-b + math.sqrt(discremenet))/(2*a))
    print("second root is : ", (-b - math.sqrt(discremenet))/(2*a))
