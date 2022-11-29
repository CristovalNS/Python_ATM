from customer import Customer
import csv

class Bank:
    def __init__(self, bankName=""):
        self.__customers = []
        self.__numOfCustomers = 0
        self.__bankName = bankName

    def addCustomer(self, firstName, lastName):
        self.__customers.append(Customer(firstName, lastName))
        self.__numOfCustomers += 1

    def getNumOfCustomers(self):
        return self.__numOfCustomers

    def getCustomer(self, index):
        return self.__customers[index]