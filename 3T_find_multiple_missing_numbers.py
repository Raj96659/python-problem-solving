'''
Multiple Missing Numbers

You are given a list of integers from 1 to n, but this time more than one number may be missing.
Write a program to find all missing numbers.

👉 Example:
Input: [1, 2, 4, 6]
Here n = 6 → Expected numbers: [1,2,3,4,5,6]
Output: [3, 5]

''

a = [3, 5, 6, 8]
my_list = []
for i in range(a[0],a[-1]+1):
    my_list.append(i)
final_answer = []
for i in my_list:
    if i not in a:
        final_answer.append(i)
final_answer
