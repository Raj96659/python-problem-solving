#  Write a Python program to find the sum of all items in a dictionary.
my_dict = {
 'a': 10,
 'b': 20,
 'c': 30,
 'd': 40,
 'e': 50
 }

sum = 0
for val in my_dict.values():
    sum = sum + val
print(sum)
