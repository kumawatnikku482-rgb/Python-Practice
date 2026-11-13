
# Project: Online Shopping Discount System
#
# Task:
# 1. Take order amount and customer type as input.
# 2. If order amount is 5000 or more:
#       Premium customer gets 20% discount.
#       Regular customer gets 10% discount.
# 3. If order amount is 2000 or more but less than 5000,
#    give 5% discount.
# 4. If order amount is less than 2000, give no discount.
# 5. If order amount is zero or negative, print Invalid order amount.
# 6. Calculate discount amount and final amount.
# 7. Display order amount, discount amount and final amount.

order_amount = float(input("Enter order amount: "))
customer_type = input("Enter customer type: ")

if order_amount <= 0:
    print("Invalid order amount")

else:
    if order_amount >= 5000 and customer_type == "premium":
        discount = 0.20

    elif order_amount >= 5000 and customer_type == "regular":
        discount = 0.10

    elif order_amount >= 2000:
        discount = 0.05

    else:
        discount = 0.0

    discount_amount = order_amount * discount
    final_amount = order_amount - discount_amount

    print("Order amount:", order_amount)
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)
