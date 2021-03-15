#ladder if else - : if you have many consditions and you want to execute code based on those conditions . then you can use ladder if else 

a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of c: '))

if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
else:
    print("c is greater")