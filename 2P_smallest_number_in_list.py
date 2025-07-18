# Write a Python program to find smallest number in a list.

list1 = [2,4,5,1,6]

small = list1[0]

for i in list1:
    if i < small:
        small = i
print(small)

