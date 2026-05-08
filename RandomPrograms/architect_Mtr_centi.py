# An architect receives land measurements in meters
# but needs to submit them in centimeters. write a python program to convert meters to centimeters
# Program to convert meters to centimeters
# 1 meter = 100 centimeters

def meters_to_centimeters(meters):

    return meters * 100

meters = float(input("Enter the land measurement in meters: "))

centimeters = meters_to_centimeters(meters)

print(f"The land measurement in centimeters is: {centimeters} cm")
