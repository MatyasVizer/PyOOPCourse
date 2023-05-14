import random


tokens = []


def createToken():
    number = random.randint(10000, 99999)
    validateToken(number)


def validateToken(number):
    if number not in tokens:
        tokens.append(number)
        print("Success")
        return number
    else:
        print("fail")