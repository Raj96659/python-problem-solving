'''
 Create a function that takes three arguments a, b, c and returns the sum of the
 numbers that are evenly divided by c from the range a, b inclusive.
 Examples
 evenly_divisible(1, 10, 20) 
➞ 0
 # No number between 1 and 10 can be evenly divided by 20.
 evenly_divisible(1, 10, 2) 
➞ 30
 # 2 + 4 + 6 + 8 + 10 = 30
 evenly_divisible(1, 10, 3) 
➞ 18
 # 3 + 6 + 9 = 18
'''

def func(a,b,c):
    sum = 0
    for i in range(a,b+1):
        if i%c==0:
            sum = sum +i
    return sum

a = int(input('a : '))
b = int(input('b : '))
c = int(input("Enter the number to divide both : "))

result = func(a,b,c)
print(result)
