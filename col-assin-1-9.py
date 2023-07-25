#   9.Write a program to find frequency of given number k.
n = int(input("Enter the size of the array: "))
a = []
print("Enter the array elements:")
for i in range(n):
    a.append(int(input()))
k = int(input("Enter the element to be found: "))
count = 0
f = False
for i in range(n):
    if a[i] == k:
        count += 1
        f = True
if not f:
    print("\nGiven element is not present")
else:
    print(f"Element {k} is present {count} times")