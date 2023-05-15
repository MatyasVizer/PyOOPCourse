import random


tokens = []


class Token:

    def createToken():
        number = random.randint(10000, 99999)
        Token.validateToken(number)
        return number

    def validateToken(number):
        if number not in tokens:
            tokens.append(number)
            return number
        else:
            Token.createToken()
