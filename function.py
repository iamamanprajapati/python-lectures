#Create a function in python

# a = int(input("Enter First Number : "))
# b= int(input("Enter Second Number : "))



# def add(a,b):
#     return (a+b)


# print(add(a,b))


#find volume of cuboid

# l = int(input("Enter value of l : "))
# b = int(input("Enter value of b : "))
# h = int(input("Enter value of h : "))

# def volume(l,b,h):
#     return l*b*h

# print("The Volume of Cuvoid : ",volume(l,b,h))

#write a programm to create two functions area and paremeter of rectangle




l = int(input("Enter value of l : "))
b = int(input("Enter value of b : "))

def area(l,b):
    return l*b

def paremeter(l,b):
    return 2*(l+b)

print("Area of Rectangle",area(l,b))
print("Paremeter of Rectangle",paremeter(l,b))

