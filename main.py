# Take two integers as input
a, b = map(int, input().split())

# Display the values before swapping
print(f" a = {a}, b = {b}")

# Swap the values using XOR bitwise operation
a = a ^ b
b = a ^ b
a = a ^ b

# Display the values after swapping
print(f" a = {a}, b = {b}")
