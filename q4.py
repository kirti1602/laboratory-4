# Capitalize the first and last character of each word in a string
str = input("Enter a string: ")

# Split the string into words
words = str.split()

# Loop through each word
capitalized_words = []
for word in words:
    # Capitalize first and last character of each word
    if len(word) > 1:
        capitalized_word = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        capitalized_word = word.upper()  # If it's a single character word
    capitalized_words.append(capitalized_word)

# Join the words back into a string
result = " ".join(capitalized_words)
print("Resulting String:", result)
