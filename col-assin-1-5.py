#   5.Write a program insert a new element in array at given location k.
n = int(input("Enter the size of the array: "))
a = [0] * n
print("Enter the array elements:")
for i in range(n):
    a[i] = int(input())
element = int(input("Enter the element to be inserted: "))
k = int(input("Enter the position of the new element: "))
if k <= n:
    n = n + 1
    a.insert(k - 1, element)
    print("\nArray elements are:")
    for i in range(n):
        print(a[i], end=" ")
    print()
else:
    print("\nPosition not found")