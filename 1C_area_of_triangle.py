#  Write a Python program to find the area of a triangle.

# If two sides are given

l = int(input("Enter the length : "))
b = int(input("Enter the breadth : "))

area = 0.5 * l * b

print("Area of triangle is :",area)

# If three sides are given (Heron Formula)

x = 12
y = 14
z = 16

print(x,y,z)

s = (x+y+z)/2

area1 = (s*(s-x)*(s-y)*(s-z))**0.5

print(f'Area of triangle for three sides is {area1:.2f}')
