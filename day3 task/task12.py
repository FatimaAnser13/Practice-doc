
# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiplication(a, b):
    return a * b

# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Menu function
def menu():

    while True:

        print("\n===== Calculator =====")
        print("Operations: +, -, *, /")

        operation = input("What do you want to do? (+, -, *, /): ")

        # Validate operation
        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation! Please select +, -, *, /.")
            continue

        # Take numeric inputs
        try:
            a = int(input("Enter first value: "))
            b = int(input("Enter second value: "))

        except ValueError:
            print("Invalid input! Enter integer values.")
            continue

        # Perform calculation
        if operation == "+":
            result = add(a, b)

        elif operation == "-":
            result = subtract(a, b)

        elif operation == "*":
            result = multiplication(a, b)

        elif operation == "/":
            result = divide(a, b)

        # Display result
        print("Result:", result)

        # Continue or exit
        choice = input("Enter 'y' to continue or 'e' to exit: ").lower()

        if choice == "y":
            continue

        elif choice == "e":
            print("Exit the calculator.")
            break

        else:
            print("Invalid choice! Please enter y or e.")


# Call menu function
menu()
