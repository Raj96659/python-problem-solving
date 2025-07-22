'''
 Write a program that accepts a sentence and calculate the number of letters and
 digits. Suppose the following input is supplied to the program:
 hello world! 123
 Then, the output should be:
 LETTERS 10
 DIGITS 3
'''

user = input("Enter the string : ")

count_alpha = 0
count_num = 0
for i in user:
    if i.isalpha():
        count_alpha = count_alpha + 1
    elif i.isdigit():
        count_num = count_num + 1


print("LETTERS",count_alpha)
print("DIGITS",count_num)
