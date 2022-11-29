from pre_menu import Pre_Menu
from IPython.display import display
import pandas as pd
import csv

class Admin_Menu:
    def __init__(self, user_input=Pre_Menu):
        self.__user_input = user_input

    def admin_selected_option(self):
        admin_password = "thisisntastrongpassword"
        input_password = input("Please input the Admin password > ")

        if input_password == admin_password:
            x = "Admin access granted."
            print("-" * len(x))
            print(x)
            print("-" * len(x))
            return admin_password
        else:
            # print("Password is incorrect! Terminating Process.")
            print("[ERROR]")

    def admin_main_menu(self):
        print("Welcome to the Admin page.")
        print("\t(1) View Customers")
        print("\t(2) Search Customers")
        print("\t(3) Add Customer")
        print("\t(4) Edit Customer")
        print("\t(5) Remove Customer")
        print("\t(0) Exit Program")
        self.__user_input = input("Enter the appropriate number to proceed > ")

        if self.__user_input == "1":
            data = pd.read_csv('customer_names.csv')
            print("Viewing All Customer Data:")
            print("Total Customers = ", len(data))
            print(data)
            print("")
            next_action = input("Would you like to do another action? (Y/N) > ").casefold()
            if next_action == "y":
                Admin_Menu().admin_main_menu()
            else:
                print("Terminating Admin program.")

        if self.__user_input == "2":
            data = pd.read_csv('customer_names.csv', sep=',')
            df = pd.DataFrame(data)
            user_input = int(input("Search customer based on their registered number > "))
            print(f"Displaying data of customer number {user_input}: ")
            display(df.iloc[user_input])
            print("")
            next_action = input("Would you like to do another action? (Y/N) > ").casefold()
            if next_action == "y":
                Admin_Menu().admin_main_menu()
            else:
                print("Terminating Admin program.")

        if self.__user_input == "3":
            print("Adding a new customer through admin.")
            with open('customer_names.csv', 'a') as csv_file:
                username = input("Enter the customer's username > ")
                password = input("Enter the customer's temporary password > ")
                re_password = input("Re-enter the customer's temporary password > ")
                if re_password == password:
                    pass
                else:
                    print("Password does not match, redirecting to main Admin page.")
                    Admin_Menu().admin_main_menu()

                firstname = input("Enter the customer's first name > ")
                lastname = input("Enter the customer's last name > ")
                balance = input("Enter the customer's starting balance > ")
                account_creation = [username, password, firstname, lastname, balance]
                writer_object = csv.writer(csv_file)
                writer_object.writerow(account_creation)
                print("New account successfully added through admin.")
                print("")
                next_action = input("Would you like to do another action? (Y/N) > ").casefold()
                if next_action == "y":
                    Admin_Menu().admin_main_menu()
                else:
                    print("Terminating Admin program.")

        if self.__user_input == "4":
            data = pd.read_csv('customer_names.csv')
            df = pd.DataFrame(data)
            print("Editing a customer information.")
            print("Displaying customer list:")
            print(data)
            admin_input = int(input("Select a customer based on their number ID to edit > "))

            print(f"Proceeding to edit customer number {admin_input}")
            display(df.iloc[admin_input])
            x = "Type in a variable to update (Username, Password, FirstName, LastName, Balance): "
            print("-" * len(x))

            edit_index = input("Type in a variable to update (Username, Password, FirstName, LastName, Balance) > ")
            if edit_index == "Balance":
                confirm_edit = float(input("Type in the new data > "))
            else:
                confirm_edit = input("Type in the new data > ")

            df.loc[admin_input, edit_index] = confirm_edit

            df.to_csv("customer_names.csv", index=False)

            print("Data successfully edited.")
            print(data)
            print("")
            next_action = input("Would you like to do another action? (Y/N) > ").casefold()
            if next_action == "y":
                Admin_Menu().admin_main_menu()
            else:
                print("Terminating Admin program.")

        if self.__user_input == "5":
            data = pd.read_csv('customer_names.csv')
            print("Removing a customer.")
            print("Displaying customer list:")
            print(data)

            lines = list()
            admin_input = input("Please enter a member's name to be deleted.")
            with open('customer_names.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    lines.append(row)
                    for field in row:
                        if field == admin_input:
                            lines.remove(row)

            with open('customer_names.csv', 'w') as writeFile:
                writer_r = csv.writer(writeFile)
                writer_r.writerows(lines)

            print("Customer successfully deleted.")
            print("")
            next_action = input("Would you like to do another action? (Y/N) > ").casefold()
            if next_action == "y":
                Admin_Menu().admin_main_menu()
            else:
                print("Terminating Admin program.")

        elif self.__user_input == "0":
            print("Terminating Admin program.")

        elif self.__user_input not in ("1", "2", "3", "4", "5"):
            print("Invalid option. Please type in the appropriate number.")
            self.admin_main_menu()





