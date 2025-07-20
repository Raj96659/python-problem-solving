#  Write a Python program to print odd numbers in a List.

list2 = list(map(int,input("Enter the list : ").split()))

result = [i for i in list2 if i%2==1]
print(result)
