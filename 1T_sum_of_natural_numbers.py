#  Write a Python Program to Find the Sum of Natural Numbers.

num = int(input("Enter the number : "))

sum = 0

while num > 0:
    sum = sum + num
    num = num - 1

print(sum)
