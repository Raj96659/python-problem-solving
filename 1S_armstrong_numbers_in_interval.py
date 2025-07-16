# Write a Python Program to Find Armstrong Number in an Interval.
start = int(input("Start : "))
last = int(input("Last : "))

while start <= last:
    n = start
    sum = 0
    diglen = len(str(n))
    arm = n
    while n > 0:
        r = n % 10
        sum = sum + (r**diglen)
        n = n // 10
    if sum == arm:
        print(arm,'is Armstrong')
    start = start + 1
