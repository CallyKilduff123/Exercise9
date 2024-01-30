# Step 2: Type the following code:
var = input("Please enter a value: ")
# This is an easy way of outputting a prompt to the console and getting a reply.
# The variable var is a reference to that reply, which is a string.

# Step 3: Print the following:
# a) The value of var as upper case. By adding .upper(), I can convert the input in var to upper case
print("a) Value of var in upper case:", var.upper())

# b) The number of characters in var (this does not require a method).
# By using len (a Python built-in function), I can count the number of character in var
print("b) Number of characters in var:", len(var))


# c) Does it contain numeric characters? (try the isdecimal() method).
# by using isdecimal(), I can check if var contains any decimal

# print("c) Does it contain numeric characters?", var.isdecimal())

# .isnumeric() can also be used to achieve the same result
# Allows a broader range of numeric characters
# Including decimal digits, superscripts, subscripts, and other numeric symbols

# print("c) Does it contain numeric characters?", var.isnumeric())

# Both .isnumeric() and .isdecimal() only return true if ALL the input values are numeric
# If there are both numeric and string values, it returns False
# Can define new function so that if ANY numeric values are present then will return True
# Define new function has_numeric so that for any characters (char) in var that are numeric,
# it returns true
def has_numeric():
    for char in var:
        if char.isnumeric():
            return True
    return False


# Use if statement so that if function has_numeric returns true/false, print the appropriate response
if has_numeric():
    print(f"c) Does it contain numeric characters? {has_numeric()}")
else:
    print(f"c) Does it contain numeric characters? {has_numeric()}")
