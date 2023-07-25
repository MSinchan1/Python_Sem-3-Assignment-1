#   7.Write a program to remove duplicate elements from an array
n = int(input("Enter number of terms : "))
arr = []
print("Enter the elements :")
for i in range(n):
    arr.append(int(input()))
arr1 = []
for j in arr:
    if j not in arr1:
        arr1.append(j)
print("Array after removing duplicate element")             
print(' '.join(map(str,arr1)))