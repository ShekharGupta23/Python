# Input sales for today and yesterday
today_sales = float(input("Enter today's sales: "))
yesterday_sales = float(input("Enter yesterday's sales: "))

sales_sum = today_sales + yesterday_sales
sales_difference = today_sales - yesterday_sales
sales_product = today_sales * yesterday_sales
sales_division = today_sales / yesterday_sales if yesterday_sales != 0 else "Undefined (division by zero)"
sales_remainder = today_sales % yesterday_sales if yesterday_sales != 0 else "Undefined (division by zero)"

print(f"Sum of sales: {sales_sum}")
print(f"Difference of sales: {sales_difference}")
print(f"Product of sales: {sales_product}")
print(f"Division result: {sales_division}")
print(f"Remainder: {sales_remainder}")
