import token


accounts = dict()


class Account():
    def __init__(self, Name, Deposit, accNumber):
        self.name = Name
        self.deposit = Deposit
        self.number = accNumber


def createAccount():
    print("Please type your name:")
    try:
        name = str(input())
    except ValueError:
        print("\nWrong input type, please try again")
        createAccount()
    print("Please input the size of the deposit:")
    try:
        deposit = int(input())
    except ValueError:
        print("\nWrong input type, please try again")
        createAccount()
    accountNumber = token.createToken()
    accounts["{accountNumber}"] = Account(name, deposit, accountNumber)
    print("Your account has been successfully created!")
    accountDetails.printAccountDetails(accounts["{accountNumber}"])


def validateAccount():
    print("Please type your name:")
    try:
        name = str(input())
    except ValueError:
        print("\nWrong input type, please try again")
        validateAccount()
    print("Please input your account number:")
    try:
        accNumber = int(input())
    except ValueError:
        print("\nWrong input type, please try again")
        validateAccount()
    storedName = accountDetails.getName(accounts["{accNumber}"])
    storedNumber = accountDetails.getNumber(accounts["{accNumber}"])
    if name == storedName & accNumber == storedNumber:
        return None


class accountDetails():

    def printAccountDetails(self):
        print("\nAccount details:")
        print(f"\nName: {self.name}")
        print(f"\nDeposit: ${self.deposit}")
        print(f"\nAccount Number: {self.number}")

    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.name
