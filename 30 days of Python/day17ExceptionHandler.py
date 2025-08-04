# expenses = []

# def add_expense():
#     try:
#         name = input("Enter expense name: ")
#         amount = float(input("Enter amount: "))
#         if amount < 0:
#             raise ValueError("Amount cannot be negative")
#         expenses.append((name, amount))
#     except ValueError as e:
#         print("Invalid input:", e)

# def show_report():
#     try:
#         if not expenses:
#             raise Exception("No expenses found.")
#         total = sum([amount for _, amount in expenses])
#         print("\nExpense Report:")
#         for name, amount in expenses:
#             print(f"{name}: ${amount}")
#         print("Total:", total)
#     except Exception as e:
#         print("Error:", e)

# while True:
#     print("\n1. Add Expense\n2. Show Report\n3. Exit")
#     choice = input("Choose an option: ")

#     if choice == '1':
#         add_expense()
#     elif choice == '2':
#         show_report()
#     elif choice == '3':
#         break
#     else:
#         print("Invalid choice.")




# def Farconverter():
#     try:
#         temp = float(input("Enter Temprature"))
#         if type(temp) != float:
#             raise TypeError("Please enter a float type")
#         value = 9/5(temp) - 32
#         return value
#     except TypeError as e:
#         print("Invalid Type:" , e)


# def CelConverter():
#     try:
#         temp= float(input("Enter Temprature: "))
#         if type(temp) != float:
#             raise TypeError("Please enter a float type")
#         value = 5/9(temp) + 32
#         return value
#     except TypeError as e:
#         print("Invalid Type:" , e)


# while True: 
#     print("\n1. Convert to Faranite\n2. Convert to celisius\n3. Exit")
#     choice =  input("choose an option: ")

#     if choice == '1':
#       Farconverter()
#     elif choice =='2':
#       CelConverter()
#     elif choice == '3':
#       break
#     else: 
#         print("Invalid choice")

# #gpt solution
# def celsius_to_fahrenheit():
#     try:
#         temp = float(input("Enter temperature in Celsius: "))
#         fahrenheit = (temp * 9/5) + 32
#         print(f"{temp}°C is {fahrenheit:.2f}°F")
#     except ValueError:
#         print("Invalid input: Please enter a numeric value.")

# def fahrenheit_to_celsius():
#     try:
#         temp = float(input("Enter temperature in Fahrenheit: "))
#         celsius = (temp - 32) * 5/9
#         print(f"{temp}°F is {celsius:.2f}°C")
#     except ValueError:
#         print("Invalid input: Please enter a numeric value.")

# while True:
#     print("\n1. Convert Celsius to Fahrenheit")
#     print("2. Convert Fahrenheit to Celsius")
#     print("3. Exit")
#     choice = input("Choose an option: ")

#     if choice == '1':
#         celsius_to_fahrenheit()
#     elif choice == '2':
#         fahrenheit_to_celsius()
#     elif choice == '3':
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter 1, 2, or 3.")



# 🔧 Exercise 2: Simple Calculator
# Build a calculator that:

# Asks the user for two numbers and an operator (+, -, *, /)

# Performs the calculation

# Handles ZeroDivisionError, ValueError, and unknown operator


def calculate():

    try:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        operator=input("Enter operator: ")
        if operator=='+':
            return num1+num2
        elif operator=='-':
            return num1-num2
        elif operator=='*':
            return num1 * num2
        elif operator=='/':
            return num1/num2
        else:
            raise TypeError("Invalid operator")
    except ValueError as e:
        print("Invalid input:",e)
    except ZeroDivisionError as e:
        print("Division by zero:",e)


    

#with gpt
def calculate():
    try:
        num1 = float(input("Enter your first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter your second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise TypeError("Invalid operator. Use +, -, *, or /.")
        print(f"Result: {num1} {operator} {num2} = {result}")
    
    except ValueError:
        print("Invalid input: Please enter valid numbers.")
    except ZeroDivisionError as zde:
        print("Math error:", zde)
    except TypeError as te:
        print("Operator error:", te)

# Run the calculator in a loop
while True:
    calculate()
    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Goodbye!")
        break


