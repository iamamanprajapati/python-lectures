class Rundog:
    def bark(self):
        print('Vedansh..............')
        print('Bhow......Bhow.......')
    
    def growl(self):
        print('Vidit..........')
        print('mmmm..........mmmm............')
    
class Bulldog(Rundog):
    def growl(self):
        print('Aditya..........')
        print('mmmm..........mmmm............')

dog = Bulldog()
# ref = Rundog()
# ref.growl()
dog.growl()
dog.bark()