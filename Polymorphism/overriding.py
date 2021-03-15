class A:
    def m1(self):
        print("m1 method of A")

    def m2(self):
        print("m2 method of A")

class B(A):
    def m1(self):
        print("m1 of B")

obj = B()
obj.m1()


        
