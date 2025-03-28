# Example 1: Removing leading whitespace
text1 = "   Hello, World!   "
stripped_text1 = text1.lstrip()
print(f"Original: '{text1}'")
print(f"Stripped: '{stripped_text1}'")

#Example 2: Removing specific characters
text2 = "www.example.com"
stripped_text2 = text2.lstrip("w.")
print(f"Original: '{text2}'")
print(f"Stripped: '{stripped_text2}'")