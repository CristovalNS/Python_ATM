from login import Login, Register, Begin, Access, CurrentUser
from IPython.display import display
from account import Account
import csv
import pandas as pd

class Customer_Menu:

    def __init__(self, user_input="x"):
        self.__user_input = user_input

    def customer_menu_options(self):
        print("Welcome to your bank account,", CurrentUser() + ".")
        print("\t(1) View Account Balance")
        print("\t(2) Deposit Cash")
        print("\t(3) Withdraw Cash")
        print("\t(4) Edit Account Details")
        print("\t(0) Exit Program")
        self.__user_input = input("Enter the appropriate number to proceed > ")

        if self.__user_input == "1":
            filename = open('customer_names.csv', 'r')
            file = csv.DictReader(filename)

            username = []
            balance = []

            for col1 in file:
                username.append(col1['Username'])
                balance.append(col1['Balance'])

            # To check the contents of the list
            # print('Username:', username)
            # print('Balance:', balance)

            user_username = str(CurrentUser())
            x = username.index(user_username)
            user_balance = balance[x]

            # To check the value of the variables
            # print("TEST=Index of HappyBasil =", x)
            # print("TEST=Balance of HappyBasil =", balance[x])

            user_account = Account(user_balance)
            print("Your current balance is:", user_account.getBalance())

            filename.close()

            next_action = input("Would you like to do another action? (Y/N) > ").casefold()
            if next_action == "y":
                Customer_Menu().customer_menu_options()
            else:
                print("Thank you for using this ATM system! ^v^")

        elif self.__user_input == "2":

            filename = open('customer_names.csv', 'r')
            file = csv.DictReader(filename)

            username = []
            balance = []

            for col1 in file:
                username.append(col1['Username'])
                balance.append(col1['Balance'])

            user_username = str(CurrentUser())
            x = username.index(user_username)
            user_balance = balance[x]

            user_account = Account(user_balance).getBalance()
            print("Your current balance is: ", user_account)
            deposit_amount = float(input("Enter the amount you wish to deposit > "))
            print(f"About to deposit {deposit_amount}")

            confirmation = input("Confirm? (Y/N) > ").casefold()
            if confirmation == "y":
                result = Account(float(user_balance)).deposit(deposit_amount)
                print(f"Amount deposited - {deposit_amount}")
                updated_balance = float(user_account) + deposit_amount
                print("Updated balance - {}".format(updated_balance))

                filename.close()

                data = pd.read_csv('customer_names.csv')
                df = pd.DataFrame(data)

                df.loc[x, 'Balance'] = float(user_account) + deposit_amount

                df.to_csv("customer_names.csv", index=False)

            else:
                print("Transaction cancelled.")

            next_action = input("Would you like to do another action? (Y/N) > ").casefold()
            if next_action == "y":
                Customer_Menu().customer_menu_options()
            else:
                print("Thank you for using this ATM system! ^v^")

        elif self.__user_input == "3":
            filename = open('customer_names.csv', 'r')
            file = csv.DictReader(filename)

            username = []
            balance = []

            for col1 in file:
                username.append(col1['Username'])
                balance.append(col1['Balance'])

            user_username = str(CurrentUser())
            x = username.index(user_username)
            user_balance = balance[x]

            user_account = Account(user_balance).getBalance()
            print("Your current balance is: ", user_account)
            withdraw_amount = float(input("Enter the amount you wish to withdraw > "))
            print(f"About to withdraw {withdraw_amount}")

            confirmation = input("Confirm? (Y/N) > ").casefold()
            if confirmation == "y":
                result = Account(float(user_balance)).withdraw(withdraw_amount)
                print(f"Amount withdraw - {withdraw_amount}")
                updated_balance = float(user_account) - withdraw_amount
                print("Updated balance - {}".format(updated_balance))

                filename.close()

                data = pd.read_csv('customer_names.csv')
                df = pd.DataFrame(data)

                df.loc[x, 'Balance'] = float(user_account) - withdraw_amount

                df.to_csv("customer_names.csv", index=False)

            else:
                print("Transaction cancelled.")

            next_action = input("Would you like to do another action? (Y/N) > ").casefold()
            if next_action == "y":
                Customer_Menu().customer_menu_options()
            else:
                print("Thank you for using this ATM system! ^v^")

        elif self.__user_input == "4":
            filename = open('customer_names.csv', 'r')
            file = csv.DictReader(filename)

            username = []
            balance = []

            for col1 in file:
                username.append(col1['Username'])
                balance.append(col1['Balance'])

            user_username = str(CurrentUser())
            x = username.index(user_username)

            data = pd.read_csv('customer_names.csv')

            print(f"Current Account Details: ")
            df = pd.DataFrame(data)
            display(df.iloc[x])

            print("-" * 83)

            edit_index = input("Type in a variable to update (Username, Password) > ")
            if edit_index == "Username":
                confirm_edit = str(input("Type in your new Username: "))
                df.loc[x, edit_index] = confirm_edit

                df.to_csv("customer_names.csv", index=False)

                print("Data successfully edited.")

            elif edit_index == "Password":
                while True:
                    confirm_edit = str(input("Type in your new Password: "))
                    retype_edit = str(input("Re-type in your new Password: "))

                    if retype_edit == confirm_edit:
                        df.loc[x, edit_index] = confirm_edit
                        df.to_csv("customer_names.csv", index=False)
                        print("Data successfully edited.")
                        break
                    else:
                        print("Passwords does not match. Please type again.")

            else:
                print("[ERROR]: Variable not allowed/recognized]")
                print("Redirecting to main page.")
                Customer_Menu().customer_menu_options()

            next_action = input("Would you like to do another action? (Y/N) > ").casefold()
            if next_action == "y":
                Customer_Menu().customer_menu_options()
            else:
                print("Thank you for using this ATM system! ^v^")

        elif self.__user_input == "0":
            print("Thank you for using this ATM system! ^v^")
