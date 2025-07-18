#  Write a Python program to find second largest number in a list.

list1 = list(map(int,input("Enter the list element : ").split()))

list1.sort(reverse=True)

print("Second Largest element in List is : ",list1[1])
