#  Write a Python Program to Check Prime Number.

num = int(input("Enter the Number : "))

is_prime = True

for i in range(2,num):
    if num%i==0:
        is_prime = False
        break

if is_prime:
    print(num,"is prime number")
else:
    print(num,"is not prime number")
