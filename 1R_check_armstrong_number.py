# Write a Python Program to Check Armstrong Number?

num = int(input("Enter the number : "))
sum = 0
diglen = len(str(num))
arm = num

while num>0:
    r = num % 10
    sum = sum + (r**diglen)
    num = num // 10

if sum == arm:
    print(arm,"is armstrong")
else:
    print(arm,"is not armstrong")
