# Write a Python Program to find largest element in an array

arr = list(map(int,input("Enter the list elements : ").split()))

max_el = arr[0]

for i in arr:
    if i > max_el:
        max_el = i

print(max_el)

