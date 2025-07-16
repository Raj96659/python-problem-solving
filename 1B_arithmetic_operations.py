 # Write a Python program to do arithmetical operations addition and division.

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

add = a + b

print(f"Addition of {a} and {b} is {add}")

if b==0:
    print("Cannot divide by 0")
else:
    div = a/b    
    print(f"Division of {a} by {b} is {div}")
