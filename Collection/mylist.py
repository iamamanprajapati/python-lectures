# list1 = ["Manish","Aman", "Amit","Prashant" ]

# # print(list1[0], "'s", "Sallary is ", list1[3])
# print(type(list1))
# print(list1)
# print(type(list1[0]))

# for i in list1:
#     print(i)

list1 = []
print("Enter name of your five friends : ")

for i in range(5):
    name = input()
    list1.insert(i, name)

print(list1.sort())

for i in list1:
    print(i)


# print(list1.sort)
