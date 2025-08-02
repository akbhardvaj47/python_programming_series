# -------------------------------
# 📘 What is a String?
# -------------------------------
# A string is a sequence of characters enclosed in single, double, or triple quotes.

text = 'Python Programming'
text1 = "I love Python"
intro = """Hello
my name is Amit
I love coding"""

print(text)
print(text1)
print(intro)

# -------------------------------
# 🔢 String Indexing and Slicing
# -------------------------------
# Index:        0123456789101112131415161718
# Text:        'Python Programming'

print("\nSlicing Examples:")
print(text[1:4])      # yth
print(text[:])        # Full string
print(text[0:6:2])    # Pto

print("\nCharacter Access:")
print(text[0])        # P
print(text[9])        # o

print(text[-1])       # g
print(text[-9])       # g

# -------------------------------
# ➕ String Concatenation and Repetition
# -------------------------------
first_name = "Alok"
last_name = "Sharma"
full_name = first_name + " " + last_name
print("\nFull name:", full_name)

name = "Alok"
print(name * 10)
print("*" * 10)

# -------------------------------
# 🔠 String Case Methods
# -------------------------------
text = "Python Programming"
print("\nCase Methods:")
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())
print(text.swapcase())

# -------------------------------
# 🔍 String Search Methods
# -------------------------------
text = "I love coding in python"
print("\nSearching Characters:")
print("First 'o' at:", text.find('o'))
print("Last 'o' at:", text.rfind('o'))
print("Find 'z':", text.find('z'))  # Returns -1 if not found

# print(text.index('c'))          # Raises ValueError if not found
# print(text.index('z'))

# -------------------------------
# 🔁 Replace and Count
# -------------------------------
print("\nReplace and Count:")
print(text.replace("python", "Java"))
print("Count of 'o':", text.count('o'))

# -------------------------------
# ✅ String Checks
# -------------------------------
name = "hello"

print("\nCharacter Type Checks:")
print("Is alpha:", name.isalpha())
print("Is digit:", name.isdigit())
print("Is alphanumeric:", name.isalnum())
print("Is space:", name.isspace())
print("Is lowercase:", name.islower())
print("Is uppercase:", name.isupper())

print("Starts with 'He':", name.startswith("He"))
print("Ends with 'lo':", name.endswith("lo"))

# -------------------------------
# 📏 Length, Min, Max
# -------------------------------
name = "Amit"
print("\nLength, Min, Max:")
print("Length of string:", len(name))
print("Minimum character:", min(name))
print("Maximum character:", max(name))

# -------------------------------
# 🧾 String Formatting
# -------------------------------
age = 22
print("\nString Formatting:")
print("Name: %s, Age: %d" % (name, age))              # Old style
print("My name is {} and my age is {}".format(name, age))  # str.format()
print(f"My name is {name} and my age is {age}")       # f-string

# -------------------------------
# 🔡 Escape Characters
# -------------------------------
print("\nEscape Characters:")
print("I love \"python\"")
print("Name\tAmit")
print("My name is Amit\nMy age is 22")

# -------------------------------
# ❌ Strings are Immutable
# -------------------------------
text = "Hello"
# text[0] = 'h'  # ❌ Not allowed
text = 'hello'
print("\nUpdated string:", text)

# -------------------------------
# 🔠 Character Comparison
# -------------------------------
print("\nCharacter Comparison:")
print('a' == 'b')      # False
print(ord('a'))        # 97
print(ord('b'))        # 98
print('a' < 'b')       # True
print('a' > 'b')       # False
print('b' != 'y')      # True

a = "hello"
b = "world"
print("String Comparisons:")
print(a == b)
print(a != b)
print(a < b)
print(a > b)

# -------------------------------
# 🔍 Membership Operators in Strings
# -------------------------------
sub1 = "Python"
sub2 = "java"

print("Membership Operators:")
print("on in sub1:", "on" in sub1)     # True
print("on in sub2:", "on" in sub2)     # False
print("on not in sub2:", "on" not in sub2)  # True
