# Display the menu
print("Welcome to the Calculator Restaurant!")
print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take the customer's choice
choice = int(input("Please choose an option (1-4): "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == 1:
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif choice == 2:
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif choice == 3:
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid option from the menu.")
