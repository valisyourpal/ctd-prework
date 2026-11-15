# Favorite Ice Cream Flavor Based on Your Age Quiz

# Ask user for their information
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Ice Cream determinator
if age <= 10:
    print("Hi, " + name + "!" + " You are " + str(age) + " years old and your favorite ice cream flavor is bubble gum.")
elif age <= 20:
    print("Hi, " + name + "!" + " You are " + str(age) + " years old and your favorite ice cream flavor is oreo.")
elif age > 20:
    print("Hi, " + name + "!" + " You are " + str(age) + " years old and your favorite ice cream flavor is vanilla.")

# Example run 1
# Inputs: Bella, 11
# Output: Hi, Bella! You are 11 years old and your favorite ice cream flavor is oreo.

# Example run 2
# Inputs: Juan, 30
# Output: Hi, Juan! You are 30 years old and your favorite ice cream flavor is vanilla.
