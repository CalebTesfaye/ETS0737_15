# Example 1: Removing trailing whitespace
text1 = "   Hello, World!   "
stripped_text1 = text1.rstrip()
print(f"Original: '{text1}'")
print(f"Stripped: '{stripped_text1}'")

# Example 2: Removing specific characters
text2 = "www.example.com"
stripped_text2 = text2.rstrip(".com")
print(f"Original: '{text2}'")
print(f"Stripped: '{stripped_text2}'")