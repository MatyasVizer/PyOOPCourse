import accounts


def logIn():
    print("Press 1 to open a new account, press 2 to open an existing one")
    try:
        choice = int(input())
    except ValueError:
        print("\nWrong input type, please try again.")
        logIn()
    try:
        if choice == 1:
            account = accounts.createAccount()
            return account
        elif choice == 2:
            account = accounts.validateAccount()
            return account
        else:
            print("\nWrong number, please try again.")
    except NameError:
        print("\nError occured during login, please try again.")
        logIn()
