# Write a Python program to check if a given string is binary string or not

user_input = "1001110"
flag = 1
for i in user_input:
    if i not in '01':
        flag=0
if flag:
    print('Binary')
else:
    print('Not Binary')
