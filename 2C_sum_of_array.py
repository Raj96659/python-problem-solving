#  Write a Python Program to find sum of array

arr = list(map(int,input("Enter the list elements : ").split()))
sum = 0

for i in arr:
    sum = sum + i

print(sum)
