class Employee:
    def setEmployee(self, empId, empName):
        self.empId = empId
        self.empName = empName

    def getEmplaoyee(self):
        return self.empId, self.empName


class Payroll(Employee):
    def setPayroll(self, bs, hra, da):
        self.bs = bs
        self.hra = hra
        self.da = da

    def getPayroll(self):
        return self.bs, self.hra, self.da


class Loan:
    def setLoan(self, amt):
        self.amt = amt

    def getLoan(self):
        return self.amt


class Payslip(Payroll, Loan):
    def netSalary(self):
        print("Net Salary = ", self.bs + self.hra+self.da)
        print("Salary on hand = ", self.bs + self.hra+self.da-self.amt)


payslip = Payslip()

payslip.setEmployee("1", "Aman")

a = payslip.getEmplaoyee()
print("Employee Id = ", a[0])
print("Employee Name = ", a[1])

payslip.setPayroll(50000, 60000, 70000)

b = payslip.getPayroll()
print("Basic Salary = ", b[0])
print("House Rent Allownces = ", b[1])
print("Dearless Allownses = ", b[2])

payslip.setLoan(100000)

print("Loan = ", payslip.getLoan())

payslip.netSalary()
