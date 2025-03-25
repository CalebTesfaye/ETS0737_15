text = "Hello, World!"

print(text.endswith("World!"))  # Output: True
print(text.endswith("world!"))  # Output: False (case-sensitive)
print(text.endswith("Hello"))  # Output: False

filename = "document.txt"

if filename.endswith((".txt", ".pdf", ".docx")):
    print("This is a document file.")
else:
    print("This is not a document file.")
