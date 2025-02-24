# Display the smallest word in a string
str = input("Enter a string: ")

# Split the string into words
words = str.split()

# Find the smallest word by length
smallest_word = min(words, key=len)

print(f"The smallest word in the string is: {smallest_word}")
