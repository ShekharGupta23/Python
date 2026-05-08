# A mechanical engineer is designing a circular gear.
# write a python program to calculate its perimeter and area using radius.

radius = float(input("Enter the radius of the gear: "))

perimeter = 2 * 3.14159 * radius
area = 3.14159 * radius * radius

print("Perimeter of the gear: {:.2f}".format(perimeter))
print("Area of the gear: {:.2f}".format(area))
