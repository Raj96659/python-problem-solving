#  Write a Python program to print even numbers in a list

# list1 = list(map(int,input("Enter the list element : ").split()))

# for i in list1:
#     if i%2==0:
#         print(i,'is even number')


list2 = list(map(int,input("Enter the list : ").split()))

result = [i for i in list2 if i%2==0]
print(result)
