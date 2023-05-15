import accounts


def logIn():
    print("Press 1 to open a new account, press 2 to open an existing one")
    try:
        choice = int(input())
    except ValueError:
        print("\nWrong input type, please try again.")
        logIn()
    if choice == 1:
        accounts.createAccount()
    elif choice == 2:
        accounts.validateAccount()
    else:
        print("\nWrong number, please try again.")
