#  Write a Python program to Remove empty List from List.

list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]

final_list = []

for i in list_of_lists:
    if len(i) != 0:
        final_list.append(i)
print(final_list) 
