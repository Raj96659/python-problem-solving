'''
Write a program that accepts a sequence of whitespace separated words as input
 and prints the words after removing all duplicate words and sorting them
 alphanumerically.
 Suppose the following input is supplied to the program:
 hello world and practice makes perfect and hello world again
 Then, the output should be:
 again and hello makes perfect practice world
'''

# Accept input and split into words
user = list(map(str, input("Enter the string: ").split()))
print(user)

# Remove duplicates using set
no_duplicate = set(user)
print(no_duplicate)

# Convert set to list and sort
set_to_list = sorted(list(no_duplicate))
print(set_to_list)

# Print the sorted unique words
print(" ".join(set_to_list))
