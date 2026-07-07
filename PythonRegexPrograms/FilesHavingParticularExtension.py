import re
fn = ["gfg.html", "geeks.xml", "computer.txt", "geeksforgeeks.jpg"]

for file in fn:
    match = re.search(r"\.xml$", file)
    if match:
        print("The file ending with .xml is:", file)