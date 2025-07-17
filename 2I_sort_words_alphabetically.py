#  Write a Python Program to Sort Words in Alphabetic Order.

input_string = input("Enter the string : ")

split_string = [i.capitalize() for i in input_string.split()]

split_string.sort()

for wd in split_string:
    print(wd)
