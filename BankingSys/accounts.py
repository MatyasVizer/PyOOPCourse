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
    _printAccountDetails(accounts["{accountNumber}"])


def _printAccountDetails(object):
    print("\nAccount details:")
    print(f"\nName: {object.name}")
    print(f"\nDeposit: ${object.deposit}")
    print(f"\nAccount Number: {object.number}")
