
class Pre_Menu:
    def __init__(self, user_input="x"):
        self.__user_input = user_input

    def selected_option(self):
        print("Welcome to the ATM system.")
        print("Please select an option by typing the appropriate number:")
        print("\t(1) Customer")
        print("\t(2) Admin")
        self.__user_input = input("Enter selection: ")
        # print(self.__user_input) #TODO: Testing input value

        if self.__user_input == '1':
            x = "Selected: Customer"
            print("-" * len(x))
            print(x)
            print("-" * len(x))
            return self.__user_input
        elif self.__user_input == '2':
            x = "Selected: Admin"
            print("-" * len(x))
            print(x)
            print("-" * len(x))
            return self.__user_input
        else:
            x = "Invalid input. Please enter the correct input."
            print("-" * len(x))
            print(x)
            print("-" * len(x))
