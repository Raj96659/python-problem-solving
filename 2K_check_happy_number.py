# Write a Python program to check if the given number is Happy Number

'''
 19 is a Happy Number because:

 1**2 + 9**2 = 81
 8**2 + 2**2 = 68
 6**2 + 8**2 = 100
 1**2 + 0**2 + 0**2 = 1

 The process reaches 1, so 19 is a Happy Number

'''

num = int(input("Enter the number : "))
seen = set()


while num!=1 and num not in seen:
    seen.add(num)
    sum = 0
    for i in str(num):
        sum = sum + int(i)**2
    #print(sum)
    num = sum

if num == 1:
    print('happy')
else:
    print('not happy')
