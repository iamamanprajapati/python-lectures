class Shape:
    def setValue(self, a):
        self.a = a


class Square(Shape):
    def square(self):
        return self.a*self.a


class Cube(Shape):
    def volume(self):
        return self.a*self.a*self.a


obj1 = Square()
a = int(input("Enter value : "))
obj1.setValue(a)
print("Area of square : ", obj1.square())


obj2 = Cube()
obj2.setValue(a)
print("Volume of cube : ", obj2.volume())
