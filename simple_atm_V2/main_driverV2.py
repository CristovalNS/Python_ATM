from pre_menu import Pre_Menu
from admin_menu import Admin_Menu
from login import Begin, Access, Login, CurrentUser, Register
from customer_menu import Customer_Menu
import csv

filename = open('customer_names.csv', 'r')
file = csv.DictReader(filename)

username_password = []

for col1 in file:
    username_password.append(col1['Username'])
    username_password.append(col1['Password'])

# print(username_password) # Testing

while True:
    x = Pre_Menu().selected_option()
    if x == "1":
        y = Begin(), Access()
        if CurrentUser() not in username_password:
            break
        else:
            z = Customer_Menu().customer_menu_options()
            break

    elif x == "2":
        attempts = 0
        while attempts < 3:
            y = Admin_Menu().admin_selected_option()
            if y == "thisisntastrongpassword":
                y = Admin_Menu().admin_main_menu()
                break
            else:
                attempts += 1
                print(f"Incorrect password. {attempts} out of 3 attempts used.")
                if attempts == 3:
                    print("Program terminated.")
        break

    else:
        continue
