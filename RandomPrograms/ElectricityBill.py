# Python program to calculate electricity bill based on units consumed
units = float(input("Enter the number of units consumed: "))

# Initialize bill amount
bill = 0

if units <= 100:
    bill = units * 5         # First 100 units at Rs.5/unit
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7  # Next 100 units at Rs.7/unit
elif units <= 300:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10  # Next 100 units at Rs.10/unit
else:
    bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15  # Above 300 units at Rs.15/unit

# Apply surcharge for bills above Rs. 2000
if bill > 2000:
    surcharge = 0.10 * bill  # 10% surcharge
    bill += surcharge

print(f"Your electricity bill is: Rs. {bill:.2f}")