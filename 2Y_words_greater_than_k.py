#  Write a Python program to find words which are greater than given length k.

word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon"]
len_word = 5

for i in word_list:
    if len(i) >= len_word:
        print(i,end=' ')
