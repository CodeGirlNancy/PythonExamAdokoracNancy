# WITU Sacco
class WITUSacco:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        if amount >= 1000:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Minimum deposit amount is 1000.")
    
    def withdraw(self, amount):
        if amount >= 500:
            if self.balance >= amount:
                self.balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Minimum withdrawal amount is 500.")
    
    def check_balance(self):
        print("Your Sacco account balance is:", self.balance)


def main():
    sacco = WITUSacco()
    print("Welcome, WITU Sacco")
    
    while True:
        print("\nOptions:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            sacco.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            sacco.withdraw(amount)
        elif choice == '3':
            sacco.check_balance()
        elif choice == '4':
            print("Thank you for Serving WITU Sacco.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
