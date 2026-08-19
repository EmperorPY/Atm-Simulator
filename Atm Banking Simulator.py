money = 500

menu = input("Welcome\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n")
    
def print_menu():
    print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")




def deposit(money):
    try:
        deposit = int(input("How much do you want to deposit?"))
        print(f"You have deposited £{deposit}")
        money += deposit
    except ValueError:
        print("Please enter a valid number.")
    return money

        
    

def withdraw(money):

        try:
            withdraw = int(input("How much do you want to withdraw?"))

            if withdraw > money:
             print("Insufficient funds.")
            else:
                money -= withdraw
                print(f"You have withdrawn £{withdraw}")

        except ValueError:
            print("Please enter a valid number.")
        return money

def check_balance(money):
    print(f"Your balance is £{money}")
    return money



while True:
    
    if menu == "1":
        money = deposit(money)
        print_menu()
        menu = input("")
    elif menu == "2":
        money = withdraw(money)
        print_menu()
        menu = input("")
    elif menu == "3":
        money = check_balance(money)
        print_menu()
        menu = input("")
    elif menu == "4":
        print("Thank you for using our ATM")
        break
    else:
        print("Invalid input")
        print_menu()
        menu = input("")
    
