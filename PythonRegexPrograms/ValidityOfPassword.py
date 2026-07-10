import re

password = "R@m@_f0rtu9e$"
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@$])[A-Za-z\d_@$]{8,}$"

if re.fullmatch(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")