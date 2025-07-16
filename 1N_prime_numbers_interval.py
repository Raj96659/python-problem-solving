# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.

first_interval = int(input("Enter first interval : "))
last_interval = int(input("Enter last interval : "))

for num in range(first_interval,last_interval+1):

    is_prime = True

    for j in range(2,num):
        if num%j==0:
            is_prime = False
            break

    if is_prime:
        print(num,"is prime number")
