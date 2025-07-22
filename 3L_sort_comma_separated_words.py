'''
 Write a program that accepts a comma separated sequence of words as input and
 prints the words in a comma-separated sequence after sorting them alphabetically.
 Suppose the following input is supplied to the program:
 without,hello,bag,world
 Then, the output should be:
 bag,hello,without,world
'''

user_input = list(map(str,input("Enter the string : ").split()))

print("Before Sorting : ",user_input)

user_input.sort()

print("After Sorting : ",user_input)
