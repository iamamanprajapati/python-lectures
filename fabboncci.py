n1 = 0
n2 = 1

n  = int(input("How many terms do you want to series : "))

print('Fibonacci series')

print(n1)
print(n2)

i = 1

while(i<=n-2):
    n3 = n1+n2
    print(n3)
    n1=n2
    n2=n3
    i=i+1

