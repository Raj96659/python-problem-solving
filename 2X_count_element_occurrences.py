#  Write a Python program to Count occurrences of an element in a list

list1 = [1,2,2,3,2,4,5]
element = 2
count = 0

for i in list1:
    if i == element:
        count = count + 1
print(count)
