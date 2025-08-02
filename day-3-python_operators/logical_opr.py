# Logical Operator 

a=10
b=20

print(a>0 and b>5)  # True

print(a<5 or b>5)    # true

print(a>30 or b>30)   # false

print(not a>=10)      # false

print(not b==20)     # False

print(not a==20)  # True

# Another Example

a = True
b = False

print("a =", a)
print("b =", b)

# Logical AND
print("a and b:", a and b)  # True only if both are True

# Logical OR
print("a or b:", a or b)    # True if at least one is True

# Logical NOT
print("not a:", not a)      # Inverts the value of a
print("not b:", not b)      # Inverts the value of b

# More practical examples
x = 5
y = 10

print("\nx =", x)
print("y =", y)

# Check if x is greater than 0 and less than 10
print("x > 0 and x < 10:", x > 0 and x < 10)

# Check if x is less than 0 or y > 5
print("x < 0 or y > 5:", x < 0 or y > 5)

# Using not
print("not (x > y):", not (x > y))
