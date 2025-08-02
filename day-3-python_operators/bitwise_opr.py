# Bitwise Operator in python

a = 5
b = 2

print(bin(a))  # 0101
print(bin(b))  # 0010

print(bin(a&b),a & b)   # 0000

print(a|b)     # 0111  # 7

print(a^b)     # 0111

print(~a)      

print(a<<1)     # 0101  # 1010 # 10
print(a>>1)     # 0101   # 0010 # 2

# Another example

a = 10  # In binary: 1010
b = 4   # In binary: 0100

print("a =", a, "=", bin(a))
print("b =", b, "=", bin(b))

# Bitwise AND
print("a & b =", a & b, "=", bin(a & b))

# Bitwise OR
print("a | b =", a | b, "=", bin(a | b))

# Bitwise XOR
print("a ^ b =", a ^ b, "=", bin(a ^ b))

# Bitwise NOT
print("~a =", ~a, "=", bin(~a))  # Note: ~a = -(a + 1)

# Left Shift
print("a << 1 =", a << 1, "=", bin(a << 1))  # Multiply by 2

# Right Shift
print("a >> 1 =", a >> 1, "=", bin(a >> 1))  # Divide by 2
