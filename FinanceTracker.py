transactions = []
balance = 0

print("Welcome to Simple Finance Tracker!")

while True:
    print("\nWhat would you like to do?")
    print("1. Add Money")
    print("2. Spend Money")
    print("3. Check Balance")
    print("4. See All Transactions")
    print("5. Quit")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "1":
        amount = float(input("How much money did you get? "))
        reason = input("Where did it come from? ")
        transactions.append(f"+${amount} from {reason}")
        balance += amount
        print(f"Added ${amount} to your balance!")
    
    elif choice == "2":
        amount = float(input("How much did you spend? "))
        reason = input("What did you spend it on? ")
        transactions.append(f"-${amount} on {reason}")
        balance -= amount
        print(f"Subtracted ${amount} from your balance.")
    
    elif choice == "3":
        print(f"\nYour current balance is: ${balance}")
    
    elif choice == "4":
        print("\nAll Transactions:")
        for t in transactions:
            print(t)
    
    elif choice == "5":
        print("\nGoodbye! Here's your final report:")
        print(f"Final Balance: ${balance}")
        print("Your Transactions:")
        for t in transactions:
            print(t)
        break
    
    else:
        print("Please enter a number between 1-5")