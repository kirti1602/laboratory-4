# Accept two strings and display common words
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Convert both strings into sets of words
words1 = set(str1.split())
words2 = set(str2.split())

# Find common words
common_words = words1.intersection(words2)

if common_words:
    print("Common words:", common_words)
else:
    print("No common words found.")
