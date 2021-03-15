empid = int(input("Enter emp id : "))
empname = input("Enter emp name : ")
salary = int(input("Enter emplaoyee salary"))

f = open('employee.txt','w')
f.write(str(empid))
f.write(empname)
f.write(str(salary))

f.close()