string1 = "   "
print(string1.isspace())  # Output: True
string2 = "\t\n\r"
print(string2.isspace())  # Output: True
string3 = "  Hello  "
print(string3.isspace())  # Output: False (contains non-whitespace characters)
string4 = ""
print(string4.isspace()) # Output: False (empty string)