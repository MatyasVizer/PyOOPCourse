import token


accounts = dict()


class Account():
    def __init__(self, Name, accNumber, Password):
        self.name = Name
        self.balance = 0
        self.number = accNumber
        self.password = Password
        self.state = "logged_out"
        self.sessionId = "none"

    def deposit(cls):
        print("Please input the size of the deposit:")
        try:
            deposit = int(input())
        except ValueError:
            print("\nWrong input type, please try again")
            deposit()
        if deposit > 0:
            cls.balance += deposit
        else:
            print("Please input a value bigger than 0.")
            deposit()

    def withdraw(cls):
        print("Please input the size of the withdrawal:")
        try:
            withdraw = int(input())
        except ValueError:
            print("\nWrong input type, please try again.")
            withdraw()
        if withdraw > 0:
            cls.balance -= withdraw
        else:
            print("Please input a value bigger than 0.")
            withdraw()

    def printAccountDetails(cls):
        print("\nAccount details:")
        print(f"\nName: {cls.name}")
        print(f"\nDeposit: ${cls.deposit}")
        print(f"\nAccount Number: {cls.number}")

    def getPassword(cls):
        return cls.password

    def getNumber(cls):
        return cls.name
    
    def logged_in(cls):
        cls.state = "logged_in"
        cls.sessionId = token.generateSessionId

    def logged_out(cls):
        cls.state = "logged_out"
        cls.sessionId = "None"


def createAccount():
    print("Please type your name:")
    try:
        name = str(input())
    except ValueError:
        print("\nWrong input type, please try again")
        createAccount()
    print("Please type your password:")
    try:
        password = str(input())
    except ValueError:
        print("\nWrong input type, please try again")
        createAccount()
    accountNumber = token.createToken()
    accounts["{accountNumber}"] = Account(name, accountNumber, password)
    print("\nYour account has been successfully created!\nPlease log in to your account.")
    accountDetails.printAccountDetails(accounts["{accountNumber}"])
    validateAccount()


def validateAccount():
    print("\nPlease input your account number:")
    try:
        accNumber = int(input())
    except ValueError:
        print("\nWrong input type, please try again")
        validateAccount()
    print("\nPlease input your password number:")
    try:
        password = int(input())
    except ValueError:
        print("\nWrong input type, please try again")
        validateAccount()
    storedNumber = Account.getNumber(accounts["{accNumber}"])
    storedPassword = Account.getPassword(accounts["{accNumber}"])
    if accNumber == storedNumber & password == storedPassword:
        return accounts["{accNumber}"]
    else:
        print("\nYour password or your account number was incorrect, please try again.")
        validateAccount()


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
