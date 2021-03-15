class MyClass:
    #When we use method inside class then we have to use a default parameter in method.
    def sayHello(self,name):
        print("Hello ",name)

#Here we test the class

m = MyClass()
n = input("Enter your name : ")
m.sayHello(n)
