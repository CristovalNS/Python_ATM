from account import Account

class Customer:
    def __init__(self, firstName="", lastName=""):
        self.__firstName = firstName
        self.__lastName = lastName

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAccount(self):
        return self.__account

    def setAccount(self, account):
        self.__account = account




