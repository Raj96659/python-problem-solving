#  Write a Python Program to check if a string contains any special character.

# Define special characters
special_sym = '''!@#$%^&*()_+{}[]:;<>,.?~\\/'"-=|'''

# Take user input
user_input = input("Enter a string: ")

# Check for special characters
for char in special_sym:
    if char in user_input:
        print("The string contains special characters.")
        break
else:
    print("No special characters found.")
