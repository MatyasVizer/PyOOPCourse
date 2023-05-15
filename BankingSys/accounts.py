import tokenizer as token


accounts = dict()


class Account():
    def __init__(self, Name, accNumber, Password):
        self.name = Name
        self.balance = 0
        self.number = accNumber
        self.password = Password
        self.state = "logged_out"

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
        cls.accountActions()

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
        cls.accountActions()

    def printAccountDetails(cls):
        print("\nAccount details:")
        print(f"\nName: {cls.name}")
        print(f"\nBalance: ${cls.balance}")
        print(f"\nAccount Number: {cls.number}")
        print(f"\nPassword: {cls.password}")

    def getPassword(cls):
        return cls.password

    def getNumber(cls):
        return cls.name

    def logged_in(cls):
        cls.state = "logged_in"

    def logged_out(cls):
        cls.state = "logged_out"

    def getBalance(cls):
        print(f"This is your balance: ${cls.balance}")

    def accountActions(cls):
        print("\nWelcome to Account Actions. Please type 1 to get your account balance.")
        print("\nPlease type 2 if you would like to deposit funds and type 3 if you would like to withdraw money")
        print("\nPlease type 4 if you would like to quit the application.")
        try:
            choice = int(input())
        except ValueError:
            print("\nWrong input type, please try again.")
            cls.accountActions()
        try:
            if choice == 1:
                cls.getBalance()
                cls.accountActions()
            elif choice == 2:
                cls.deposit()
            elif choice == 3:
                cls.withdraw()
            else:
                print("\nWrong number, please try again.")
        except NameError:
            print("\nError occured during login, please try again.")
            cls.accountActions()


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
    accountNumber = token.Token.createToken()
    accounts[accountNumber] = Account(name, accountNumber, password)
    print("\nYour account has been successfully created!\nPlease log in to your account.")
    Account.printAccountDetails(accounts[accountNumber])
    validateAccount()
    return accounts[accountNumber]


def validateAccount():
    print("\nPlease input your account number:")
    try:
        accNumber = int(input())
        account = accounts[accNumber]
    except ValueError:
        print("\nWrong input type, please try again")
        validateAccount()
    print("\nPlease input your password:")
    try:
        password = str(input())
    except ValueError:
        print("\nWrong input type, please try again")
        validateAccount()
    try:
        storedPassword = account.getPassword()
        print(f"Storedpw: {storedPassword}")
        if password == storedPassword:
            account.logged_in()
            return account
        else:
            print("\nYour password or your account number was incorrect, please try again.")
            validateAccount()
    except NameError:        
        print("\nSomething went wrong, please try again")
        validateAccount()

