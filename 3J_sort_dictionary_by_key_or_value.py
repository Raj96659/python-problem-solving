# Write a Python program to sort Python Dictionaries by Key or Value.

# sort by keys
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
ordered = dict(sorted(sample_dict.items()))

for key,val in ordered.items():
    print(f'{key}:{val}')

print()

# Sort by values
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

# Sorting by values using lambda function
sorted_dict_by_values = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

print("Sorted by values:")
for key, value in sorted_dict_by_values.items():
    print(f"{key}: {value}")
