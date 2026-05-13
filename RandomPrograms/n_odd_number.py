# A game assigns odd- numbered IDs to players. Write a program to find the nth odd number.

n = int(input("Enter the position (n): "))

nth_odd_number = 2 * n - 1

print(f"The {n}th odd number is: {nth_odd_number}")
