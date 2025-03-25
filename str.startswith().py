#Check the beginning
result1 = text.startswith("Python")
print(f"Starts with Python: {result1}")  # Output: True

#Check from position 7
result2 = text.startswith("prog", 7)
print(f"Starts with prog from 7: {result2}")  # Output: True

# Check for multiple prefixes
result3 = text.startswith(("Python", "Java"))
print(f"Starts with Python or Java: {result3}")  # Output: True

