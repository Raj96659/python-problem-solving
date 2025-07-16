#  Write a Python Program to Print the Fibonacci sequence.

a = 0
b = 1
term = int(input("Enter the terms to return : "))

print(a,b,end=' ')

count = 2

while count < term:
    c = a + b
    print(c,end= ' ')
    a = b
    b = c
    count = count + 1
