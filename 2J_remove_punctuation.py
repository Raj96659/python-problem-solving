#  Write a Python Program to Remove Punctuation From a String

input_str = input("Enter the string : ")
punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''

no_punct = ""

for i in input_str:
    if i not in punctuations:
        no_punct = no_punct + i
print(no_punct)
