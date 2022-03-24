class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Thank you, (self.age) year old, (self.name.title())"

class Bank(User):
    total_deposits = 0
    total_withdraws = 0

    def _init_(self, name, age):
        super()._init_(name,age)
        self.balance = balance

    def show_info(self):
        return f"(self.name) has a renaming balance of: $(round(self.balance, 2)"

    def deposit(self):
        dp = float(input (F"(self.name.title)), please enter how many you would like to deposit"))
        print("Thank you for depositing...")
        self.balance += dp
        self.total_deposits += 1
        return f"Your balance is now: (round(self.balance, 2))"

    def withdraws(self):
        wd = float(input(f"(self.name.title()), please enter how much would you like to withdraw"))
        if self.balance < wd:
            return "You can't withdraw that amount"
        else:
            print("Thank you for withdrawing...")
            self.balance -= wd
            self.total_withdraws += 1

def options(user_two):
    print("Thank you for creating your bank account")
    print("Here are a list of options, please choose the number you want")
    while True:
        options_choice = int(input("1) See balance/n2) Withdraw/n3) Deposits/n4) See Total Withdraw/n5) See Total Deposits/n6) Quit/n"))
        if options_choice == 1:
            print(user.one_bank.show_inmfo())
            if options_choice == 1 and user_two != None:
                print(user_two.bank.show_info())
        elif options_choice == 2:
            print(user_one_bank.withdraws())
            if options_choice == 2 and user_two != None:
                wd = input(f"(user_two.name) would you like to withdraw? Yes or No:")
                if wd.lower() == 'yes':
                    print(user_two.bank.withdraws())
        elif options_choice == 3:
            print(user_one.bank.deposit())
            if options_choice == 3 and user_two != None:
                dep = input(f"(user_two.name) would you like to deposit? Yes or no:")
                if dep.lower() == 'yes':
                    print(user_two.deposit())
        elif options_choice == 4:
            print(f"There have been (user_one.bank.total_withdraws) withdraws.")
            if options_choice == 4 and user_two != None:
                print(f"(user_one.bank.total_withdraws) withdraws.")
        elif options_choice == 5:
            print(f" There have been (user_one_bank.total_deposits) deposits.")
            if options_choice == 5 and user_two != None:
                print(f"There have been (user_two.bank.total_deposits) deposits.")
        elif options_choice == 6:
            print("Thank you for using Salim's Bank")
            return False
            break
        else:
            print("Please choose a number from 1-6")

def bank_creation(name):
    balance = float(input(f"(name.name.title()), how much money do you have? "))
    return balance

while True:
    print("Welcome to Salim's Bank")
    name = input("Enter your name")
    age = int(input("Enter you age"))
    user_one = User(name, age)
    user_two = None
    new_user = input("would you like to register a new person? Type 'No' to create your bank")
    if new_user.lower() == 'yes':
        name = input("Enter the second person's name:")
        age = int(input("Enter the second person's age"))
        user_two = User(name,age)
        print("thank you for registering 2 people.Please create your bank accounts.")
        user_one_balance = bank_creation(user_one.name)
        user_two_balance = bank_creation(user_two.name)
        user_one.bank = bank(user_one.name, user_one.age, user_one_balance)
        user_two.bank = bank(user_two.name, user_two.age, user_two_balance)
        flag = options(user_two)
        if flag == False:
            break
    else:
        user_one_balance = bank_creation(user_one.name)
        user_one_bank = Bank(user_one.name, user_one.age, user_one_balance)
        flag = options(user_two)
        if flag -- False:
            break