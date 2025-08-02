# Example: Type casting in Python

# Getting input from user (always as string)
age_str = input("Enter your age: ")

# Convert string to integer
age_int = int(age_str)

# Now you can do numeric operations
print("Your age plus 5 is:", age_int + 5)
print("Type after casting:", type(age_int))

# Convert integer back to string
age_str_again = str(age_int)
print("Age as string again:", age_str_again)
print("Type after casting back:", type(age_str_again))

# Convert string to float
height_str = input("Enter your height in meters (e.g., 1.75): ")
height_float = float(height_str)
print("Your height plus 0.1 meters is:", height_float + 0.1)
print("Type of height after casting:", type(height_float))
