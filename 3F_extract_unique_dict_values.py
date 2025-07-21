# Write a Python program to Extract Unique dictionary values.

my_dict = {
 'a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20}

seen = set()

for val in my_dict.values():
    seen.add(val)

result = list(seen)

print(result)
