'''
Find Missing Number in a List
Given a list of numbers from 1 to n with one missing number, find the missing number.
👉 Example:
Input: [1, 2, 4, 5]
Output: 3

'''
a = [1, 2, 4, 5]
sum_a = sum(a)

Sum = 0
for i in range(min(a),max(a)+1):
    Sum = Sum + i

missing_number = Sum - sum_a
print(missing_number)

