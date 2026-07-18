import re

password = "Qggf!@ghf3"
pattern = (
    r"^(?!.*(.)\1\1)"         
    r"(?!.*(..).*\1)"        
    r"[^\s]{9,20}$"           
)

if re.fullmatch(pattern, password):
    print("Strong Password!")
else:
    print("Weak Password!")