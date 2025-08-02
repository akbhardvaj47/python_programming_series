# Creating lists
fruits = ["Apple", "Mango", "Orange"]
print(fruits)
print("Number of fruits:", len(fruits))

numbers = [1, 2, 3, 4, 5]
print(numbers)
print("Total numbers:", len(numbers))

mixed = [1, 2, "Hello", "99.99", True]
print(mixed)

# Nested list
number = [1, 2, 3, 4, 5, [2, 3, 4]]
print(number)
print("Total items:", len(number))

# Accessing list items
fruits = ["Apple", "Mango", "Orange"]
first_fruit = fruits[0]
second_fruit = fruits[1]
third_fruit = fruits[2]
print(first_fruit, second_fruit, third_fruit)

# Negative indexing
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit, second_last)

# List slicing
fruits = ["Apple", "Mango", "Orange", "Pineapple"]
print(fruits[1:3])
print(fruits[:])
print(fruits[:2])
print(fruits[2:])
print(fruits[0:4:2])
print(fruits[-1::-2])

# append()
fruits = ["Apple", "Mango", "Orange", "Pineapple"]
print(fruits)
fruits.append("Lemon")
print(fruits)

# extend()
num1 = [1, 2, 3]
num2 = [4, 5]
num1.extend(num2)
print(num1)

# insert()
fruits.insert(2, "Banana")
print(fruits)

# remove()
fruits = ["Apple", "Mango", "Orange", "Pineapple"]
print(fruits)
fruits.remove("Orange")
print(fruits)

# pop()
fruits = ["Apple", "Mango", "Orange", "Pineapple"]
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)

# count()
fruits = ["Apple", "Mango", "Orange", "Pineapple", "Apple"]
print(fruits)
print(fruits.count("Apple"))
print(fruits.count("Orange"))

# clear()
fruits.clear()
print(fruits)

# sort()
fruits = ["Apple", "Mango", "Orange", "Pineapple", "Apple"]
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# reverse()
fruits = ["Apple", "Mango", "Orange", "Pineapple"]
print(fruits)
fruits.reverse()
print(fruits)

# copy()
copy_fruits = fruits.copy()
print(copy_fruits)
