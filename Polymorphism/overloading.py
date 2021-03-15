class Figure:
    def area(self, x=None, y=None):
        if(x != None and y != None):
            return x*y
        elif(x != None and y == None):
            return x*x
        else:
            return 0


obj = Figure()
print("Area of Rectangle : ",obj.area(5,6))
print("Area of square : " , obj.area(5))
print(obj.area())
