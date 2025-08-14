#program to determine whether a person is eligible to vote or not.if he is not eligibale,display how many years are left to become eligible
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    years_left = 18 - age
    print(f"You are not eligible to vote. You have {years_left} years left to become eligible.")17