# Input: Ask the user to enter the patient's age
age = int(input("Enter the patient's age: "))

if age < 2:
    print("The patient is an Infant.")
elif 13 <= age <= 19:
    print("The patient is a Teenager.")
elif age >= 60:
    print("The patient is a Senior Citizen.")
else:
    print("The patient falls under the Others category.")
