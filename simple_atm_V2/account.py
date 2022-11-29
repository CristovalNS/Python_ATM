class Account:
    def __init__(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.__balance += amount
            return True

    def withdraw(self, amount):
        if amount >= self.__balance:
            return False
        else:
            self.__balance -= amount
            return True
