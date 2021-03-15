class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def result(self):
        a = self.l*self.b
        p = 2*(self.l+self.b)
        return a, p

# Test the class


l = int(input("Enter length of rectangle : "))
b = int(input("Enter width of rectangle : "))

obj = Rectangle(l, b)

a, p = obj.result()

print("Area of rectangle : ", a)
print("Paremeter of rectangle : ", p)
