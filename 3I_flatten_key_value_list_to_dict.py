#  Write a Python program to convert key-values list to flat dictionary.

key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

my_dict = {}

for key,value in key_values_list:

    my_dict[key] = value

print(my_dict)
