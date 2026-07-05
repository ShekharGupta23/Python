import re
text = "Animal"

pattern = r"^[AEIOUaeiou].*"

if re.fullmatch(pattern, text):
    print("Accepted")
else:
    print("Not Accepted")