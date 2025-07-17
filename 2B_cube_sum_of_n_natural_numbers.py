 # Write a Python Program for cube sum of first n natural numbers?

num = int(input("ENTER THE NUMBER : "))

sum = 0

while num > 0:
    sum = sum + (num**3)
    num = num - 1

print(sum)
