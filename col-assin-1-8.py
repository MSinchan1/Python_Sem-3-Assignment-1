#   8.Write a program to find second highest element from an array(Do not use sorting).
n = int(input("Enter the size of the array: "))
a = []
print("Enter the array elements:")
for i in range(n):
    a.append(int(input()))
max1 = max2 = float('-inf')
for i in range(n):
    if a[i] > max1:
        max2 = max1
        max1 = a[i]
    elif a[i] > max2 and a[i] != max1:
        max2 = a[i]
print("Second highest element is:", max2)