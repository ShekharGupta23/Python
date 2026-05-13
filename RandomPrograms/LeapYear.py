# Input year from HR
year = int(input("Enter the year to check: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} had an extra working day (Leap Year).")
else:
    print(f"{year} did not have an extra working day (Not a Leap Year).")


# A leap year is a year which has 366 days (52 weeks + 2 days).
# Such years are exactly divisible by 4, e.g. 2004, 2008, 2012 etc.
# Leap years in the form of a century are exactly divisible
# by 400, e.g. 400, 800, 1200, 1600, 2000, 2400, etc.