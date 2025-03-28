# Example 1: Splitting by whitespace (default)
text1 = "Hello World This is a test"
split_text1 = text1.split()
print(f"Original: '{text1}'")
print(f"Split: {split_text1}")

# Example 2: Splitting by a specific delimiter (comma)
text2 = "apple,banana,orange"
split_text2 = text2.split(",")
print(f"Original: '{text2}'")
print(f"Split: {split_text2}")

# Example 3: Splitting by a specific delimiter (hyphen)
text3 = "one-two-three"
split_text3 = text3.split("-")
print(f"Original: '{text3}'")
print(f"Split: {split_text3}")