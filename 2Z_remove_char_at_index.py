#  Write a Python program for removing the character at ith index.

str1 = input("Enter the String : ")
index = int(input("Enter the index : "))
len_str1 = len(str1)

if index > len_str1:
     print("Index exceeding the string.")
else:
    final = str1[:index] + str1[index+1:]
    print(final)
