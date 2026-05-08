# Input: Price of the item and GST rate
price = float(input("Enter the price of the item: "))
gst_rate = float(input("Enter the GST rate (in %): "))

# Calculate GST amount
if gst_rate > 0:
    gst_amount = (price * gst_rate) / 100
    final_bill = price + gst_amount
else:
    gst_amount = 0
    final_bill = price

print(f"GST Amount: ₹{gst_amount:.2f}")
print(f"Final Bill: ₹{final_bill:.2f}")
