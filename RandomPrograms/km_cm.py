# A taxi company wants to track distance traveled in centimeters for precision. write a python program to
# convert Kilometers into centimeters
# Program to convert kilometers into centimeters
# 1 kilometer = 100,000 centimeters

def convert_km_to_cm(kilometers):

    centimeters = kilometers * 100000
    return centimeters

kilometers = float(input("Enter distance in kilometers: "))

centimeters = convert_km_to_cm(kilometers)

print(f"{kilometers} kilometers is equal to {centimeters} centimeters.")
