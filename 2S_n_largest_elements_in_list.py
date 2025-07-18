# Write a Python program to find N largest elements from a list.

list1 = list(map(int,input("Enter the list element : ").split()))

k = int(input("Enter the N largest element : "))

list1.sort(reverse = True)

print(list1[k-1])
