# A packaging company design rectangular boxes.
# Write a python program to calculate perimeter and area using length and breadth.

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
