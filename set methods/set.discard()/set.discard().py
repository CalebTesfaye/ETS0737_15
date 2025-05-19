
s = {1, 2, 3}
s.discard(2)
s.discard(99)  # Does nothing, no error
print(s)  # Output: {1, 3}