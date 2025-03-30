string1 = "HelloWorld123"
print(string1.isalnum())  # Output: True
string2 = "HelloWorld 123"
print(string2.isalnum())  # Output: False
string3 = "12345"
print(string3.isalnum())  # Output: True
string4 = "HelloWorld"
print(string4.isalnum())  # Output: True
string5 = "!@#$%"
print(string5.isalnum())  #Output: False (contains special characters)
print("".isalnum()) #Output: False (empty string)
print("123".isalnum()) #Output: True (contains only digits)
print("abc".isalnum()) #Output: True (contains only letters)