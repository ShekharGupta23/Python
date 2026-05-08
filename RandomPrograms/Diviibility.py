# Input roll number
roll_number = int(input("Enter the roll number: "))

# Check divisibility by 5 and 11
if roll_number % 5 == 0 and roll_number % 11 == 0:
    print(f"The roll number {roll_number} is divisible by both 5 and 11.")
else:
    print(f"The roll number {roll_number} is NOT divisible by both 5 and 11.")
