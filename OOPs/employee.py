class Employee:
    companyName = "Kwikitt pvt limited"  # static variables

    def setEmployee(self, empId, empName, empSalary):
        self.empId = empId
        self.empName = empName
        self.empSalary = empSalary

    def display(self):
        print(Employee.companyName)
        print("Employee Id = ", self.empId)
        print("Employee Name = ", self.empName)
        print("Employee Salary = ", self.empSalary)

# Now we test the class 
obj = Employee()
obj.setEmployee(1,"Aman Kumar",100000000000)
obj.setEmployee(4,"Deepak Kumar","$5454545454545")
obj.display()

