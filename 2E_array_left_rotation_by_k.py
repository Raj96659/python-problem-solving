# Write a Python Program for array left rotation by k steps .

def rotateLeft(arr2,d):
    len1 = len(arr2)
    d = d % len1      # in case if d>n
    return(arr2[d:]+arr2[:d])

arr2 = list(map(int,input("Enter the list of elements : ").split()))
d = int(input("Enter rotations : "))

print("Original Array is : ",arr2)
print(f"Array after {d} rotation to left is :",rotateLeft(arr2,d))
