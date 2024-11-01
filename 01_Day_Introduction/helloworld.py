# Introduction
# Day 1 - 30DaysOfPython Challenge

print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
# the power of 3^2
print(3 ** 2)  # exponential(**)
# provides the remainder
print(3 % 2)   # modulus(%)
# Floor division essentially truncates the decimal part and rounds down the result:
# For positive numbers, it rounds down to the nearest whole number.
# For negative numbers, it rounds toward the next lower integer.
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
# order of insertion, modifiable, allows duplicates
print(type([1, 2, 3]))           # List
#  order of insertion, modifiable, keys must be unique, values can be duplicate tho
print(type({'name': 'Asabeneh'}))  # Dictionary
# unordered, modifiable, no duplicates (uses union, intersection)
print(type({9.8, 3.14, 2.7}))    # Set
# order of insertion, unmodifiable, allows duplicates
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool
