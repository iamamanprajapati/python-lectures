class Bank:
    bankname = "ALLAHBAD BANK"

    def createAccount(self, accountNo, name, balance):
        self.accountNo = accountNo
        self.name = name
        self.balance = balance

    def deposite(self, accountNo, amount):
        if(self.accountNo == accountNo):
            self.balance = self.balance+amount
            print("The ammount is credited successfully ...")
        else:
            print("Account doem not exist...")

    def withdraw(self, accountNo, ammount):
        if(self.accountNo == accountNo):
            if(self.balance < ammount):
                print("Balance is low...")
            else:
                self.balance = self.balance-amount
                print("The ammount is withdraw successfully ...")
        else:
            print("Account doesm not exist...")

    def enquiry(self, accountNo):
        if(self.accountNo == accountNo):
            print("Balance Amount is = ", self.balance)
        else:
            print("The account does not exist")


obj = Bank()

print("Welcome to ", Bank.bankname)
accountNo = int(input("Enter account No : "))
name = input("Enter Account Holder Name : ")
balance = int(input("Enter opening balance : "))
obj.createAccount(accountNo, name, balance)
print("Your account has been created")


ch = 0
while(ch != 4):
    print("1) Deposite")
    print("2) Withdraw")
    print("3) Enquiry")
    print("4) Exit")
    ch = int(input())
    if(ch == 1):
        accountNo = int(input("Enter account number : "))
        amount = int(input("Enter amount to deposite : "))
        obj.deposite(accountNo, amount)
    elif(ch == 2):
        accountNo = int(input("Enter account number : "))
        amount = int(input("Enter amount to withdraw : "))
        obj.withdraw(accountNo, ammount)
    elif(ch == 3):
        accountNo = int(input("Enter account number : "))
        obj.enquiry(accountNo)
    elif(ch == 4):
        pass
    else:
        print("wrong choice")
