# A Harshad Number (or Niven Number) is an integer that is divisible by the sum of its digits.

'''
18

Sum of digits = 1 + 8 = 9
18 ÷ 9 = 2 → ✅ Harshad Number
'''


num = int(input("Enter the number to check : "))
sum=0
for i in str(num):
    sum = sum + int(i)

if num % sum == 0:
    print('harshad number')
else:
    print('not harshad number')
