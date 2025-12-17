# Personal Information Manager
# Name: Ambikesh Kushwaha
# This is my first Python project

print("================================")
print(" PERSONAL INFORMATION MANAGER ")
print("================================")
print()

# storing personal information
name = "Ambikesh Kushwaha"
age = 23
city = "Delhi"
hobby = "Learning programming"

print("Please enter your details")
print("----------------------------")

# user input
favorite_food = input("Enter your favorite food: ")
while favorite_food == "":
    print("Input cannot be empty")
    favorite_food = input("Enter your favorite food: ")

favorite_color = input("Enter your favorite color: ")
while favorite_color == "":
    print("Input cannot be empty")
    favorite_color = input("Enter your favorite color: ")

# calculation
age_in_months = age * 12

print()
print("================================")
print("        YOUR INFORMATION")
print("================================")

print("Name:", name)
print("Age:", age, "years")
print("Age in months:", age_in_months)
print("City:", city)
print("Hobby:", hobby)
print("Favorite food:", favorite_food)
print("Favorite color:", favorite_color)

print()
print("Thank you for using this program")
