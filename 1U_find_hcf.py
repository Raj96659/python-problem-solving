# Write a Python Program to Find HCF.


num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))

if num1 > num2:
    smaller = num2
else:
    smaller = num1

for i in range(1,smaller+1):
    if (num1%i==0) and (num2%i==0):
        hcf = i
print(f"HCF of {num1} and {num2} is",hcf)
