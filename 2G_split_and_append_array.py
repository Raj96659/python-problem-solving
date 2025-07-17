#  Write a Python Program to Split the array and add the first part to the end?

def addfirstlast(arr,k):
    if k>=len(arr) or k<=0:
        return arr
    else:
        first_part = arr[:k]
        last_part = arr[k:]

        result = last_part + first_part
        return result


arr = list(map(int,input("Enter the list : ").split()))
k = int(input("Splitting elements : "))

print("Original List : ",arr)
print("After : ",addfirstlast(arr,k))
