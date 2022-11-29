from account import Account
import csv

csv_filename = 'customer_names.csv'

def Login(username, password, firstname, lastname, balance):
    filename = open('customer_names.csv', 'r')
    file = csv.DictReader(filename)

    username_password = []

    for col1 in file:
        username_password.append(col1['Username'])
        username_password.append(col1['Password'])

    print(username_password)
    with open(csv_filename, "r", encoding='utf-8', newline='') as csv_file:
        for i in csv_file:
            a, b, c, d, e = i.split(",")
            b = b.strip()
            # c = c.strip()
            # d = d.strip()
            # e = e.strip()
            if username and password not in username_password:
                x = "Invalid password or account not registered yet. Please register a new account."
                print("-" * len(x))
                print(x)
                print("-" * len(x))
                break
            else:
                x = "Login Successful!"
                print("*" * len(x))
                print(x)
                print("*" * len(x))
                break


def CurrentUser():
    return username

def Register(username, password, firstname, lastname, balance):
    with open(csv_filename, "a", encoding='utf-8', newline=None) as csv_file:
        csv_file.write("\n" + username + "," + password + "," + firstname + "," + lastname + "," + balance)

def Access():
    global username
    while True:
        if option == "1":
            firstname = "filler"
            lastname = "filler"
            balance = 0
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            Login(username, password, firstname, lastname, balance)
            break
        elif option == "2":
            y = "Enter your new username and password: "
            print("-" * len(y))
            print(y)
            print("-" * len(y))
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            username = input("Enter your account username: ")
            password = input("Enter your account password: ")
            confirm_pass = input("Re-enter your password: ")
            account = input("Enter your starting balance: ")

            balance = Account(account)

            if confirm_pass == password:
                Register(username, password, firstname, lastname, str(balance.getBalance()))
                x = "Registration complete!"
                print("*" * len(x))
                print(x)
                print("*" * len(x))
                # user = Customer(firstname, lastname)
                # account = user.setAccount(Account(0))
                break
            else:
                print("Passwords does not match. Please type again.")


def Begin():
    global option
    print("Welcome Customer!")
    print("Please select an option by typing the appropriate number:")
    print("\t(1) Login")
    print("\t(2) Register")
    option = input("Enter selection: ")
    if option == "1":
        x = "Selected: Login to account"
        print("-" * len(x))
        print(x)
        print("-" * len(x))
        return option
    elif option == "2":
        x = "Selected: Register new account"
        print("-" * len(x))
        print(x)
        print("-" * len(x))
        return option
    else:
        x = "Invalid input. Please enter the correct input."
        print("-" * len(x))
        print(x)
        print("-" * len(x))
        Begin()



# Uncomment For Testing
# Begin()
# Access()
# CurrentUser()

