# Positional arguments
string1 = "My name is {} and I am {} years old.".format("Birtukan", 30)
print(string1)  # Output: My name is Birtukan and I am 30 years old.

# Keyword arguments
string2 = "My name is {name} and I am {age} years old.".format(name="Bob", age=25)
print(string2)  # Output: My name is Bob and I am 25 years old.

# Format specifiers
string3 = "Pi is approximately {:.4f}".format(3.14159)
print(string3)  # Output: Pi is approximately 3.1416

# Accessing elements by index
string4 = "Coordinates: {0[0]}, {0[1]}".format((10, 20))
print(string4)      # Output: Coordinates: 10, 20