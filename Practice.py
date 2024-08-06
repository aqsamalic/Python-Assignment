# Age assignments
anton_age = 21
beth_age = anton_age + 6
chen_age = beth_age + 20
drew_age = chen_age + anton_age
ethan_age = chen_age

# Printing the ages
print(f"Anton is {anton_age}")
print(f"Beth is {beth_age}")
print(f"Chen is {chen_age}")
print(f"Drew is {drew_age}")
print(f"Ethan is {ethan_age}")


# 2-Formatted String Interpolation

name = "Alice"
age = 30
city = "New York"

# Using f-string
sentence = f"{name} is {age} years old and lives in {city}."
print(sentence)

#3-String Manipulation

s = "hElLo WoRlD"

# Capitalize the first letter
capitalized_s = s.capitalize()

# Convert to uppercase
uppercase_s = s.upper()

# Convert to lowercase
lowercase_s = s.lower()

print(capitalized_s)
print(uppercase_s)
print(lowercase_s)

# 4-Substring 

s = "the quick brown fox jumps over the lazy dog"

# Find the index of "fox"
index_of_fox = s.find("fox")

# Count occurrences of "the"
count_the = s.count("the")

print(f"index of 'fox' is {index_of_fox}")
print(f"'the' appears {count_the} times")


#5-String Replacement

s = "I love programming in Python"

# Replace "Python" with "Java"
replaced_s = s.replace("Python", "Java")

print(replaced_s)


#6-String Splitting and Joining

s = "apple,banana,cherry,dates"

# Split into a list
split_list = s.split(',')

# Join with spaces
joined_string = ' '.join(split_list)

print(split_list)
print(joined_string)

#7-String Stripping and Justifying

s = "   Python is fun!   "

# Remove leading/trailing spaces
stripped_s = s.strip()

# Left justify with '*'
left_justified_s = stripped_s.ljust(20, '*')

# Right justify with '*'
right_justified_s = stripped_s.rjust(20, '*')

print(stripped_s)
print(left_justified_s)
print(right_justified_s)

#8-Convert an integer to its binary representation

num = 45

# Binary representation
binary_representation = bin(num)

print(f"Binary representation: {binary_representation}")

#9-Calculate Powers of Numbers.

base = 3
exponent = 4

power_result = base ** exponent

print(f"Power result: {power_result}")

#10-Round floating-point numbers

value = 12.34567

# Round to the nearest integer
rounded_int = round(value)

# Round to two decimal places
rounded_two_decimals = round(value, 2)

print(f"Rounded to nearest integer: {rounded_int}")
print(f"Rounded to two decimal places: {rounded_two_decimals}")



