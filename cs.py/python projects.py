def main():
    print("Welcome to the Simple Banking System!")
    
    # creating an account
    name = input("Enter your name: ")
    while True:
        try:
            balance = float(input("Enter your initial balance: "))
            if balance < 0:
                print("Balance cannot be negative. Please enter a valid amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    print(f"Account created successfully for {name} with balance: ${balance:.2f}\n")
    
    while True:
        # menu options
        print("Choose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            # deposting
            try:
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    print("Deposit amount must be greater than zero.")
                else:
                    balance += amount
                    print(f"${amount:.2f} deposited successfully! New balance: ${balance:.2f}\n")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                
        elif choice == "2":
            # withdrawing
            try:
                amount = float(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("Withdrawal amount must be greater than zero.")
                elif amount > balance:
                    print("Insufficient funds. Please enter a valid amount.")
                else:
                    balance -= amount
                    print(f"${amount:.2f} Sucessful withdrawl. New balance: ${balance:.2f}\n")
            except ValueError:
                print("Invalid input.")
                
        elif choice == "3":
            # checking your balance
            print(f"Current balance: ${balance:.2f}\n")
            
        elif choice == "4":
            # exiting
            print("Thank you for using the Simple Banking System. Goodbye!")
            break
            
        else:
            print("Invalid. Select a number from 1-4\n")
            
if __name__ == "__main__":
    main()
