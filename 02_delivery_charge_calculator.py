
# Project: Delivery Charge Calculator

# Problem Statement:
# Create a Python program for an online shopping website.
#
# Requirements:
# 1. Take the order amount from the customer.
# 2. If the order amount is Rs. 2000 or more,
#    delivery charge should be Rs. 0.
# 3. If the order amount is more than Rs. 1000
#    but less than Rs. 2000, delivery charge should be Rs. 40.
# 4. If the order amount is Rs. 1000 or less,
#    delivery charge should be Rs. 80.
# 5. Calculate the final amount.
# 6. Display order amount, delivery charge and final amount.

# Solution:

amount = int(input("Enter order amount: "))
delivery_charge = 0

if amount >= 2000:
    delivery_charge = 0

elif amount > 1000:
    delivery_charge = 40

else:
    delivery_charge = 80

final_amount = amount + delivery_charge

print("Order amount:", amount)
print("Delivery charge:", delivery_charge)
print("Final amount:", final_amount)
