# A carpenter measures wood piece in inches but the blueprints requires feet.
# Write a python program to convert inches to feet.
# 1 foot = 12 inches
def inches_to_feet(inches):
    feet = inches / 12
    return feet

inches = float(input("Enter the length in inches: "))
feet = inches_to_feet(inches)
print(f"{inches} inches is equal to {feet:.2f} feet.")
