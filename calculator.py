name = input("What is your Name? ")
print("Hello " + name)
print("WELCOME TO MY CALCULATOR!")
print("Select an Operator:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
     choice= input("Enter your choice: ")
         
     if choice in ['1' , '2',  '3', '4']:
        try:
            num1= float(input('First number: '))
            num2= float(input('Second number: '))
        except ValueError:
            print("Invalid input! Try Again")
            continue

        if choice == '1':
            print("The Addition is: ", num1 + num2 )
        elif choice == '2':
           print("The Subtraction is: ", num1 - num2 )
        elif choice == '3':
           print("The Multiplication is: ", num1 * num2 )
        elif choice == '4':
           print("The Division is : ", num1 / num2 )
     elif choice == '5':
         print("Thank you, see you next time!")
         break
     else:
        print("Invalid choice! Try Again!")  
