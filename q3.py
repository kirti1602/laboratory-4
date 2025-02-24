# Check if a string is a palindrome
str = input("Enter a string to check if it's a palindrome: ")

# Remove spaces and convert to lowercase for comparison
str = str.replace(" ", "").lower()

# Check if the string is equal to its reverse
if str == str[::-1]:
    print(f"'{str}' is a palindrome.")
else:
    print(f"'{str}' is not a palindrome.")
