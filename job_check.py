# 1. User se age, qualification aur experience input lo.
# 2. Age 18 ya usse zyada honi chahiye.
# 3. Qualification graduate honi chahiye.
# 4. Experience kam se kam 1 year hona chahiye.
# 5. Teeno conditions true hain → Eligible for job
# 6. Koi bhi condition false hai → Not eligible for job
# 7. Age negative ya 100 se zyada ho, ya experience negative ho → Invalid input.


age = int(input("enter your age :"))
qualification = input("enter your qualification :")
experience = int(input("enter your experience :"))

if age <= 0 or age > 100 or experience < 0:
        print("invalid input")
else :
    if (age >= 18 and qualification == "graduate" and experience >= 1) :
        print("Eligible for job")
    else :
        print("not eligible for job")



