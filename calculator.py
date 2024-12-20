
def display_menu():
    print("\nSimple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def perform_calculation(num1, num2, operation):
    if operation == "1":
        return num1 + num2
    elif operation == "2":
        return num1 - num2
    elif operation == "3":
        return num1 * num2
    elif operation == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero is not allowed."
    else:
        return "Invalid operation!"

def main():
    while True:
        display_menu()
        choice = input("\nChoose an operation (1-5): ").strip()
        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break
        elif choice in {"1", "2", "3", "4"}:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            result = perform_calculation(num1, num2, choice)
            print(f"Result: {result}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

