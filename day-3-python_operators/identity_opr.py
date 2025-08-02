# Identity operators: 'is' and 'is not'
# They compare the memory location (identity) of two objects

a="Hello"
b="World"

print(a is b)

print(a is not b)


x = [1, 2, 3]
y = [1, 2, 3]
z = x  # z references the same object as x

print("x =", x)
print("y =", y)
print("z = x")

# Check identity using 'is'
print("x is y:", x is y)   # False: different objects with same content
print("x is z:", x is z)   # True: same object in memory

# Check identity using 'is not'
print("x is not y:", x is not y)  # True
print("x is not z:", x is not z)  # False
