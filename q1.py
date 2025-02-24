# Slicing Operations in Strings
str = "Python Programming"

# Slicing the string
print("Original String:", str)

# Slicing from index 2 to 5 (not including 5)
print("Sliced String (2 to 5):", str[2:5])

# Slicing from the start to index 5 (not including 5)
print("Sliced String (Start to 5):", str[:5])

# Slicing from index 7 to the end
print("Sliced String (7 to End):", str[7:])

# Slicing the string with a step of 2 (every second character)
print("Sliced String (Step of 2):", str[::2])

# Reversing the string using slicing
print("Reversed String:", str[::-1])
