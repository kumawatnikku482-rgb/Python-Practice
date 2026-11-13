
# Project: Electricity Bill Calculator

# Problem Statement:
# 1. Customer se electricity units input lo.
# 2. if, elif, else se rate decide karo.
# 3. Total bill calculate karo.
# 4. Units, rate aur final bill print karo.

# Solution:

electricity = int(input("Enter electricity units: "))

if electricity > 200:
    rate = 10

elif electricity > 100:
    rate = 7

else:
    rate = 5

final_amount = electricity * rate

print("Electricity units:", electricity)
print("Rate per unit:", rate)
print("Final bill:", final_amount)
