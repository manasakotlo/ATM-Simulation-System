# ATM Automation Simulation - Python Micro Project

class ATM:
    def __init__(self, pin="7788", balance=2890):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def login_page(self):
        print("===== WELCOME TO ATM AUTOMATION SYSTEM =====")
        print("----------- LOGIN PAGE -----------")

        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("Login successful!\n")
                return True
            attempts -= 1
            print("Incorrect PIN! Attempts left:", attempts)

        print("Too many wrong attempts. Card blocked.")
        return False

    def menu_page(self):
        print("\n===== MAIN MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Fast Cash")
        print("7. Receipt")
        print("8. Exit")

    def check_balance(self):
        print("Available Balance: ₹", self.balance)
        self.transaction_history.append("Checked Balance")

    def deposit(self):
        amount = float(input("Enter amount to deposit: ₹"))
        self.balance += amount
        print("₹", amount, "deposited successfully")
        print("Available Balance: ₹", self.balance)
        self.transaction_history.append(f"Deposited ₹{amount}")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= self.balance:
            self.balance -= amount
            print("₹", amount, "withdrawn successfully")
            print("Available Balance: ₹", self.balance)
            self.transaction_history.append(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")
            print("Available Balance: ₹", self.balance)

    def fast_cash(self):
        amount = 500
        if self.balance >= amount:
            self.balance -= amount
            print("₹500 withdrawn successfully")
            print("Available Balance: ₹", self.balance)
            self.transaction_history.append("Fast Cash ₹500")
        else:
            print("Insufficient balance")

    def change_pin(self):
        current_pin = input("Enter current PIN: ")
        if current_pin == self.pin:
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                print("PIN changed successfully")
                self.transaction_history.append("PIN Changed")
            else:
                print("PIN must be exactly 4 digits")
        else:
            print("Wrong current PIN")

    def mini_statement(self):
        print("\n----- MINI STATEMENT -----")
        if self.transaction_history:
            for item in self.transaction_history:
                print("-", item)
        else:
            print("No transactions yet")

    def receipt_page(self):
        print("\n----- RECEIPT -----")
        print("Current Balance: ₹", self.balance)
        print("Thank you for using ATM")

def main():
    atm = ATM()

    if not atm.login_page():
        return

    while True:
        atm.menu_page()
        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            atm.deposit()
        elif choice == "3":
            atm.withdraw()
        elif choice == "4":
            atm.mini_statement()
        elif choice == "5":
            atm.change_pin()
        elif choice == "6":
            atm.fast_cash()
        elif choice == "7":
            atm.receipt_page()
        elif choice == "8":
            print("Thank you for using ATM Simulation")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
