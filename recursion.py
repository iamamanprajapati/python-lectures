num = int(input("Enter a number for factorial : "))

def fact(num):
    if (num==1 or num==0):
        return 1
    return num*fact(num-1)

print("The factorial of ",num,"is",fact(num))