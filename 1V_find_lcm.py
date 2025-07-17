#  Write a Python Program to Find LCM.

def find_hcf(a, b):
    # HCF using simple loop
    for i in range(1, min(a, b) + 1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    return hcf

def find_lcm(a, b):
    hcf = find_hcf(a, b)
    lcm = (a * b) // hcf
    return lcm

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"The LCM of {num1} and {num2} is {find_lcm(num1, num2)}")
