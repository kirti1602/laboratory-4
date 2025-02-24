# Count frequency of vowels in a string
str = input("Enter a string: ")

# Initialize vowel frequency dictionary
vowels = "aeiou"
vowel_count = {v: 0 for v in vowels}

# Loop through the string and count vowels
for char in str.lower():
    if char in vowels:
        vowel_count[char] += 1

# Display the count of each vowel
print("Vowel Frequencies:", vowel_count)
