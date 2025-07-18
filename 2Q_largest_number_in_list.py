# Write a Python program to find largest number in a list.

list1 = [2,4,5,1,6]

large = list1[0]

for i in list1:
    if i > large:
        large = i
print(large)
