# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries

# Integer variable
my_integer = 5

# Float variable
my_float = 13.2

# String variable
my_string = "This is a string"

# Boolean variable
my_boolean = True

# List variable
my_list = [0, 1, "two", 3.2, False]

# Tuple variable
my_tuple = (0, 1, 2)

# Dictionary variable
my_dict = {"one": 1, "two": 2}

# Print each variable
print(my_integer)
print(my_float)
print(my_string)
print(my_boolean)
print(my_list)
print(my_tuple)
print(my_dict)

# Re-declaring a variable works
my_integer = "abc"
print(my_integer)

# To access a member of a sequence type, use []
print(my_list[2])
print(my_tuple[1])

# Use slices to get parts of a sequence
print(my_list[1:4:2])

# You can use slices to reverse a sequence
print(my_list[::-1])

# Dictionaries are accessed via keys
print(my_dict["one"])

# ERROR: variables of different types cannot be combined
# print("string type " + 123)
print("string type " + str(123))

# Global vs. local variables in functions
def some_function():
    # Local variable
    my_string = "def"
    print(my_string)

some_function()
print(my_string)  # Global variable still intact

# Deleting a variable
del my_string
# This will raise an error since my_string is no longer defined
print(my_string)
