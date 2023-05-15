import random
import session_manager


def createToken():
    number = random.randint(10000, 99999)
    validateToken(number)
    return number


def validateToken(number):
    if number not in session_manager.tokens:
        session_manager.tokens.append(number)
        return number
    else:
        createToken()


def generateSessionId():
    id = random.randint(10000, 99999)
    validateSessionId(id)
    return id


def validateSessionId(id):
    if id not in tokens:
        tokens.append(id)
        return id
    else:
        generateSessionId()