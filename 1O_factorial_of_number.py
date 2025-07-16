#  Write a Python Program to Find the Factorial of a Number.

num = int(input("Enter the number : "))
fact = 1

num_1 = num

while num>0:
    fact = fact * num
    num = num - 1

print(f'Factorial of {num_1} is {fact}')
