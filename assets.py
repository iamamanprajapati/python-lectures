#Accepts the salary of an employee from user . Calculate gross salary on the following basics - :
# Basic                   HRA                  DA
# 1-4000                  10%                  50%
# 4001-8000               20%                  60%
# 8001-12000              25%                  70%
# 12001 to above          30%                  80%

basicSalary = int(input("Enter Basic Sallary : "))

if(basicSalary <= 4000):
    grossSallary = basicSalary + (basicSalary *10)/100 + (basicSalary*50)/100
    
elif(basicSalary > 4000 and basicSalary <=8000):
    grossSallary = basicSalary + (basicSalary *20)/100 + (basicSalary*60)/100
elif(basicSalary > 8000 and basicSalary <=12000):
    grossSallary = basicSalary + (basicSalary *25)/100 + (basicSalary*70)/100
else:
    grossSallary = basicSalary + (basicSalary *30)/100 + (basicSalary*70)/100


print('Gross Salary : ', grossSallary)