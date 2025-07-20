# Write a Python program to find all duplicate characters in string


# Input string
string = input("Enter a string: ")

# Dictionary to store character counts
char_count = {}

# Count each character
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print duplicate characters
print("Duplicate characters are:")
for char, count in char_count.items():
    if count > 1:
        print(f"'{char}' appears {count} times")
