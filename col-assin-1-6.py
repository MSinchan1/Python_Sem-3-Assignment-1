#   6.Write a program to delete an element from an array.
a = []
n = int(input("Enter the size of the array: "))
print("Enter the array elements:")
for i in range(n):
    a.append(int(input()))
element = int(input("Enter the element to be deleted: "))
f = 0
i = 0
while i < len(a):
    if a[i] == element:
        a.pop(i)
        n -= 1
        f = 1
    else:
        i += 1
if f == 1:
    print("\nArray elements are:")
    for i in range(n):
        print(a[i], end=" ")
else:
    print("Given element is not present in the array")