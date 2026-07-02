import re
s = "The price is 120 dollars, and the discount is 50, saving 70 more."
m = max(int(match.group()) for match in re.finditer(r'\d+', s))
print(m)