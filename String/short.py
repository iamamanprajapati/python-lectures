# WAP to take full name as input and display short name :-

# I/P - Aman Kumar Prajapati
# O/P -A.K.Prajapati

name = input("Enter your name : ")

list = name.split()

print('your short name : ', end="")

for i in range(len(list)):
    # print(i)
    if(i+1<len(list)):
        print(list[i][0],end='.')
    else:
        print(list[i])
    

# print(list[0][0], ".", list[1][0], ".", list[2])


# print(name[2])
